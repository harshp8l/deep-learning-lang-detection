import os
import codecs
import defs
import re
import numpy as np
import requests

train_root_folder = 'data/train'
test_root_folder = 'data/test'
snippets_per_file = 3


def get_input_and_labels(root_folder=train_root_folder, file_vector_size=10 * 1024, max_files=1000, breakup=False):
  """

  :return: X, Y
  X is a an array of inputs where each input is a padded array of quantised character one-hot vectors
  Y is basically one-hot vector of the class definition
  """
  Y = []
  langs = defs.langs
  n_classes = len(langs)
  print n_classes
  X = []
  i = 0
  for fld in langs:
    vect = [0 for x in range(0, n_classes)]
    vect[i] = 1
    print fld
    folder = os.path.join(root_folder, fld)
    n = 0
    for fn in os.listdir(folder):
      if n > max_files:
        break
      file_name = os.path.join(folder, fn)
      try:
        file_vector = turn_file_to_vector(file_name, file_vector_size, breakup=breakup)
        if len(file_vector) == snippets_per_file:  # it has been broken to snippets_per_file parts
          for fv in file_vector:
            X.append(fv)
            Y.append(vect)
        else:
          X.append(file_vector)
          Y.append(vect)
        n += 1
      except Exception as e:
        print e
    i += 1

  return np.array(X), np.array(Y)


def turn_url_to_vector(f_url, file_vector_size=10 * 1024, normalise_whitespace=True):
  r = requests.get(f_url)
  return turn_text_to_vector(r.text, file_vector_size, normalise_whitespace)

def turn_file_to_vector(file_name, file_vector_size=10 * 1024, normalise_whitespace=True, breakup=False):
  text = ""
  with codecs.open(file_name, mode='r', encoding='utf-8') as f:
    text = f.read().lower()
  if(breakup):
    return turn_text_to_vectors(text, file_vector_size, normalise_whitespace)
  else:
    return turn_text_to_vector(text, file_vector_size, normalise_whitespace)

def turn_text_to_vector(text, file_vector_size=10 * 1024, normalise_whitespace=True):
  """
  extracts feature vector from text
  :param text: text
  :param file_vector_size: size of the vector
  :param normalise_whitespace: replacing all whitespace to space
  :return: vector
  """
  file_vector = []  # will be byte array
  # Normalising whitespace
  # NOTE: this could backfire due to whitespace significant languages
  # but allows for more code consumed
  if normalise_whitespace:
    text = text.replace('\n', ' ').replace('\r', ' ').replace('\t', ' ')
    text = re.sub('\s+', ' ', text)

  text = text[0:file_vector_size]
  for ch in text:
    if ch in defs.supported_chars_map:
      file_vector.append(defs.supported_chars_map[ch])

  if len(file_vector) < file_vector_size:
    for j in range(0, file_vector_size - len(file_vector)):
      file_vector.append(defs.pad_vector)

  return np.array(file_vector)


def turn_text_to_vectors(text, file_vector_size=10 * 1024, normalise_whitespace=True):
  """
  breaks a file to 3 files if > 100 lines: second third, last third and full text
  :param text:
  :param file_vector_size:
  :param normalise_whitespace: replacing all whitespace to space
  :return: file vector or array of size 3 of file vectors
  """

  lines = text.split('\n')
  nlines = len(lines)
  if nlines > 50:
    third = nlines/snippets_per_file
    twoThird = 2*third
    text2 = '\n'.join(lines[third:twoThird])
    text3 = '\n'.join(lines[twoThird:])

    file_vectors = []  # will be array of file vectors where each is vector of a snippet

    file_vectors.append(turn_text_to_vector(text, file_vector_size, normalise_whitespace))
    file_vectors.append(turn_text_to_vector(text2, file_vector_size, normalise_whitespace))
    file_vectors.append(turn_text_to_vector(text3, file_vector_size, normalise_whitespace))
    return file_vectors
  else:
    return turn_text_to_vector(text, file_vector_size, normalise_whitespace)



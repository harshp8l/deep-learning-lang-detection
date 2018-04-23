<?php
require_once 'src/MinQueue.php';
require_once 'src/Dijkstra.php';
require_once 'src/Maze.php';

$maze = Maze::fromString(file_get_contents('maze.txt')); // < a simple text file

$start = $maze->find('S');
$goal = $maze->find('T');

$helper = new Dijkstra(
    // return neighbors
    function ($a) use ($maze) {
        return $maze->getNeighbors($a, ['W']);
    },
    // calculate the distance
    function ($a, $b) use ($maze) {
        return $maze->getDistance($a, $b);
    }
);

$tStart = microtime(true);
$path = $helper->findPath($start, $goal);
$tEnd = microtime(true);

// export the maze with the path marked with '.'
$mazeStrWithPath = $maze->toString(function ($tile) use ($path) {
    return in_array($tile, $path, true) && !in_array($tile->value, ['S', 'T'])
        ? '.'
        : $tile->value
    ;
});

printf("%s\nin: %.5fs\n\n", $mazeStrWithPath, $tEnd - $tStart);

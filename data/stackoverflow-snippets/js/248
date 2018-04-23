import People from '../views/People';
import Welcome from './../views/Welcome';
import Details from './../views/Details';
import Create from './../views/Create';

export default [
  {
    path: '/people',
    name: 'people',
    component: People,
    title: 'People',
    redirect: { name: 'people-welcome' },
    children: [
      {
        path: 'welcome',
        name: 'people-welcome',
        component: Welcome,
      },
      {
        path: 'create',
        name: 'people-create',
        component: Create,
      },
      {
        path: ':id',
        name: 'people-details',
        component: Details,
      },
    ],
  },
];

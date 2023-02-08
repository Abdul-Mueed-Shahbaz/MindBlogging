import { ROUTES } from "src/common/constants/routes";

const routes = [
  {
    path: ROUTES.LAYOUTS.BLANK_LAYOUT.PATH,
    name: ROUTES.LAYOUTS.BLANK_LAYOUT.NAME,
    component: () => import("layouts/MainLayout.vue"),
    children: [
      {
        path: ROUTES.PAGES.HOME.PATH,
        name: ROUTES.PAGES.HOME.NAME,
        component: () => import("pages/HomePage.vue"),
      },
    ],
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: ROUTES.PAGES.ERROR.PATH,
    name: ROUTES.PAGES.ERROR.NAME,
    component: () => import("pages/ErrorNotFound.vue"),
  },
];

export default routes;

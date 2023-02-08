export const ROUTES = Object.freeze({
  LAYOUTS: {
    BLANK_LAYOUT: {
      PATH: "/",
      NAME: "blanklayout",
    },
  },
  PAGES: {
    HOME: {
      PATH: "",
      NAME: "home",
    },
    ERROR: {
      PATH: "/:catchAll(.*)*",
      NAME: "error",
    },
  },
  COMPONENTS: {
    //
  },
});

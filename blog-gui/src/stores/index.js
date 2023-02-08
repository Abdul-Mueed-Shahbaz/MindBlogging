import { store } from "quasar/wrappers";
import { createPinia } from "pinia";
// import { useLoginStore } from "./login-details";

export default store(() => {
  const pinia = createPinia();

  // You can add Pinia plugins here
  // pinia.use(useLoginStore);

  return pinia;
});

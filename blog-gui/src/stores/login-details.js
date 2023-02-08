import { defineStore } from "pinia";

export const useLoginStore = defineStore("login", {
  state: () => ({
    counter: 15,
  }),

  getters: {
    doubleCount(state) {
      return state.counter * 2;
    },
  },

  actions: {
    increment() {
      this.counter++;
    },
  },
});

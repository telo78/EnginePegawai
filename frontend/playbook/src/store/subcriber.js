import store from "@/store";
import axios from "axios";
store.subscribe((mutation) => {
  switch (mutation.type) {
    case "auth/SET_TOKEN":
      if (mutation.payload) {
        axios.defaults.headers.common[
          "Authorization"
        ] = `Bearer ${mutation.payload}`;
        localStorage.setItem("token", mutation.payload);
      } else {
        axios.defaults.headers.common["Authorization"] = null;
        localStorage.removeItem("token");
      }
      break;
    case "search/SET_SEARCH":
      if (mutation.payload) {
        localStorage.setItem("search", mutation.payload.data);
      } else {
        localStorage.removeItem("search");
      }
  }
});

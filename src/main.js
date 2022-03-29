import { createApp, h, provide } from "vue";
import { createPinia } from "pinia";
import Cookies from "js-cookie";
import App from "./App.vue";
import router from "./router";
import {
  ApolloClient,
  createHttpLink,
  InMemoryCache,
} from "@apollo/client/core";
import { DefaultApolloClient } from "@vue/apollo-composable";
// import gql from "graphql-tag";

const httpLink = createHttpLink({
  uri: "http://127.0.0.1:8000/api/",
  credentials: "include",
  headers: {
    "X-CSRFToken": Cookies.get("csrftoken"),
  },
});
const cache = new InMemoryCache();
const apolloClient = new ApolloClient({
  link: httpLink,
  cache,
});

// apolloClient
//   .query({
//     query: ALL_EVENTS_QUERY,
//   })
//   .then((res) => {
//     console.log(res);
//   });

const app = createApp({
  setup() {
    provide(DefaultApolloClient, apolloClient);
  },
  render: () => h(App),
});

app.use(createPinia());
app.use(router);

app.mount("#app");

<template>
  <div class="data">
    <div>
      <h1>Events</h1>
    </div>
    <div v-for="event in result.allEvents" :key="event.id">
      {{ event.name }}
      {{ event.notes }}
      {{ event.datetime }}
    </div>
  </div>
</template>

<script>
import { useQuery } from "@vue/apollo-composable";
import gql from "graphql-tag";

export default {
  setup() {
    const ALL_EVENTS_QUERY = gql`
      query allEvents {
        allEvents {
          id
          name
          notes
          datetime
        }
      }
    `;

    const { result } = useQuery(ALL_EVENTS_QUERY);
    return { result };
  },
};
</script>

<style>
@media (min-width: 1024px) {
  .data {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>

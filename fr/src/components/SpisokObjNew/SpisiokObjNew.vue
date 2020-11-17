<template>
  <v-container>
    
  </v-container>
</template>

<script>
export default {
  data: () => ({
  e.preventDefault();
      this.$http
        .get(`http://0.0.0.0:8000/apps/accounts/logout/`, {
          headers: { Authorization: `Token ${localStorage.token}` },
        })
        .then((response) => {
          if (response.status == 200) {
            console.log(response.status);
        })
        .catch((error) => {
          console.log(error.response.data);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
  })
}
</script>
<template>
  <div class="flex items-center justify-center gap-4 h-[84vh]">
    <span class="font-bold text-9xl text-background-image">
      404
    </span>
    <USeparator orientation="vertical" size="lg" class="h-32 rounded-lg" />
    <div class="-mt-1">
      <PageTitle>
        Page Not Found
      </PageTitle>
      <p>
        Documentation guide not found.
      </p>
      <UButton
        to="/docs/introduction"
        color="primary"
        class="mt-3">
        Back to Introduction
      </UButton>
    </div>
  </div>
</template>

<script lang="ts" setup>

</script>

<style scoped>
.text-background-image {
  background-image: url("data:image/svg+xml,%3Csvg width='2250' height='900' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cg%3E%3Cpath fill='%2305df72' d='M0 0h2255v899H0z'/%3E%3Ccircle cx='366' cy='207' r='366' fill='%237bf1a8'/%3E%3Ccircle cx='1777.5' cy='318.5' r='477.5' fill='%237bf1a8'/%3E%3Ccircle cx='1215' cy='737' r='366' fill='%2300c951'/%3E%3C/g%3E%3C/svg%3E%0A");
  background-size: 110% auto;
  background-position: center;
  color: transparent;
  -webkit-background-clip: text;
  background-clip: text;
}
</style>
<template>
  <UButton to="https://github.com/glitchdevx/custos" target="_blank" color="neutral" icon="lucide:github" class="invert rounded-lg px-1.5">
    <UBadge variant="soft" color="warning" class="flex items-center gap-1 invert">
      {{ starsText }}
      <UIcon name="lucide:star" />
    </UBadge>
  </UButton>
</template>

<script lang="ts" setup>
interface PartialResponse {
  stargazers_count: number;
}

const { data: stars } = useFetch<PartialResponse>("https://api.github.com/repos/glitchdevx/custos", {
  cache: 'reload',
  ignoreResponseError: true,
  dedupe: "defer",
  key: 'github-stars'
})

const starsText = computed(() => {
  return stars.value?.stargazers_count ?? "N/A"
});

</script>

<style>

</style>
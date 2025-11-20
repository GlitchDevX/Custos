<template>
  <UButton to="https://github.com/glitchdevx/custos" color="neutral" icon="lucide:github" class="invert rounded-lg px-1.5">
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
  ignoreResponseError: true
})

const starsText = computed(() => {
  return stars.value?.stargazers_count ?? "Star on GitHub"
});

</script>

<style>

</style>
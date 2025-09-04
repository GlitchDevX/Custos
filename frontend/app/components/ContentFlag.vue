<template>
  <div class="flex flex-row gap-2">
    <UBadge
      v-for="({flag, color}, index) in coloredFlags" :key="index"
      :label="flag" :color="color" variant="subtle" class="capitalize" />
  </div>
</template>

<script lang="ts" setup>
const props = defineProps({
  flags: {
    type: Array<string>,
    required: true
  }
});

const coloredFlags = computed(() => {
  return props.flags.map((f) => {
    f = f.toLowerCase();
    const x = {
      "spam": 'warning' as const,
      "misinformation": 'info' as const,
      "harassment": 'error' as const,
      "profanity": 'error' as const,
      "other": 'neutral' as const,
    }[f] ?? 'error';

    return {flag: f, color: x}
  });
})
</script>

<style scoped>

</style>
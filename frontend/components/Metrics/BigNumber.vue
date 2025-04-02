<template>
  <div>
    <UCard class="min-w-[250px]">
      <div class="relative flex items-start flex-col">
        <span class="metric-title">{{ props.title }}</span>
        <span class="text-5xl font-bold">{{ props.number }}</span>
      </div>
    </UCard>
  </div>
</template>

<script lang="ts" setup>
const props = defineProps({
  title: {
    type: String,
    required: true
  },
  number: {
    type: Number,
    required: true
  }
});

</script>

<style scoped>
.metric-title {
  color: var(--ui-text-muted);
  position: relative;
}
</style>
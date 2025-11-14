<template>
  <UButton 
    :to="link"
    variant="outline"
    color="neutral"
    :prefetch="link !== '/api'"
    class="p-4 rounded-lg grow basis-0 flex-col items-start ring-default">
    <div class="flex flex-row gap-2 items-center">
      <UIcon :name="icon" class="text-2xl text-primary" />
      <span class="text-2xl text-primary font-semibold">
        {{ title }}
      </span>
    </div>
    <p class="text-muted">
      {{ description }}
    </p>

    <div class="grow w-full flex justify-end items-end">
      <div class="p-4 ring rounded-full ring-muted">
        <UIcon name="lucide:chevron-right" />
      </div>
    </div>
  </UButton>
</template>

<script lang="ts" setup>
defineProps({
  link: {
    type: String,
    required: true
  },
  title: {
    type: String,
    required: true
  },
  description: {
    type: String,
    required: true
  },
  icon: {
    type: String,
    required: true
  },
})
</script>

<style>

</style>
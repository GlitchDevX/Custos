<template>
  <div class="codeblock-wrapper p-4 rounded-lg relative highlighted-code max-w-full">
    <UButton v-if="showCopy" :icon="icon" variant="ghost" class="absolute top-4 right-4" @click="toClipboard" />
    <Shiki :lang="(language as any)" :code="props.content" class="overflow-x-auto thin-scrollbar" :class="`text-${props.textSize}`" />
    <slot />
  </div>
</template>

<script lang="ts" setup>
const props = defineProps({
  content: {
    type: String,
    required: true
  },
  showCopy: {
    type: Boolean,
    default: false
  },
  language: {
    type: String,
    default: ""
  },
  textSize: {
    type: String,
    default: "sm"
  }
});

const icon = ref("lucide-copy");
function toClipboard() {
  icon.value = "lucide-check";
  navigator?.clipboard?.writeText(props.content);

  setTimeout(() => {
    icon.value = "lucide-copy";
  }, 1000);
}
</script>

<style scoped>
.codeblock-wrapper {
  background: #1b1e28;
}

.thin-scrollbar {
  scrollbar-width: thin;
}
</style>
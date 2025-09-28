<template>
  <div class="codeblock-wrapper p-4 rounded-lg relative highlighted-code max-w-full max-h-full">
    <UButton v-if="showCopy" :icon="icon" variant="ghost" class="absolute top-4 right-4" @click="toClipboard" />
    <div class="max-h-full overflow-y-scroll">
      <Shiki :lang="(language as any)" :code="props.content" class="max-h-full overflow-x-auto overflow-y-scroll thin-scrollbar" :class="`text-${props.textSize}`" />
      <slot />
    </div>
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
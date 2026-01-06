<template>
  <UContainer class="p-4">
    <UCard :ui="{body: 'flex flex-row items-center gap-4'}">
      <span class="text-5xl opacity-100">
        {{ daytimeGreeting.emoji }}
      </span>
      <div class="flex flex-col">
        <h1 class="text-3xl font-black inline">
          {{ daytimeGreeting.text }}
        </h1>
        <span class="text-muted">
          {{ new Date().toDateString() }}
        </span>
      </div>
    </UCard>

    <div class="flex min-h-64 mt-4 gap-4 md:flex-row flex-col">
      <LinkCard
        link="/docs"
        title="Guides"
        icon="lucide:book-user"
        description="How to guides for Custos" />
      <LinkCard
        link="/api"
        title="API"
        icon="lucide:boxes"
        description="API referrence for all endpoints" />
      <LinkCard
        link="/playground"
        title="Playground"
        icon="lucide:send"
        description="Test out the Custos endpoints" />
      <LinkCard
        link="/config"
        title="Config"
        icon="lucide:settings"
        description="Configure Custos to suit your needs" />
    </div>


    <div class="flex flex-row gap-4 mt-4">
      <UCard class="grow-3 basis-0">
        <h2 class="font-bold text-2xl">Helpful Links</h2>
        
        <ULink class="flex items-center gap-1" to="https://github.com/glitchdevx/custos" target="_blank">
          <UIcon name="lucide:github" />
          <span>Source Code</span>
        </ULink>
        <ULink class="flex items-center gap-1" to="https://github.com/GlitchDevX/Custos/issues/new/choose" target="_blank">
          <UIcon name="lucide:bug" />
          <span>Report Bug</span>
        </ULink>
      </UCard>

      <UCard class="grow-2 basis-0">
        <h2 class="font-bold text-2xl">Version</h2>
        <span class="text-muted">
          {{ runtimeConfig.public.version }}
        </span>
      </UCard>
    </div>
  </UContainer>
</template>

<script lang="ts" setup>
import { TITLE_SUFFIX } from '~/assets/data/appData';

useSeoMeta({
  title: "Welcome" + TITLE_SUFFIX
})

const runtimeConfig = useRuntimeConfig();

const daytimeGreeting = computed(() => {
    const now = new Date().getHours()
    if (now < 6) {
      return { text: "Peacefull Night", emoji: "🌃" }
    } else if (now < 13) {
      return { text: "Good Morning", emoji: "🌅" }
    } else if (now < 18) {
      return { text: "Good Afternoon", emoji: "🏙️" }
    } else if (now < 23) {
      return { text: "Good Evening", emoji: "🌇" }
    } else {
      return { text: "Peacefull Night", emoji: "🌃" }
    }
});
</script>

<style>

</style>
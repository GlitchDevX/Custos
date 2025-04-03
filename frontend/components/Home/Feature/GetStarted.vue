<template>
    <div id="get-started" class="flex justify-center items-center">
        <div class="w-3xl">
            <div class="max-w-xl">
                <h2 class="text-3xl font-bold">
                    Start with Docker Compose
                </h2>
                <p class="muted-text">
                    You can start off by simply creating a new directory with a docker-compose.yaml and this content.
                </p>
            </div>
            <CodeBlock :content="compose" :showCopy="true" class="mt-4" />
        </div>
    </div>
</template>

<script lang="ts" setup>
import compose from '~/assets/data/docker-compose.yaml?raw';

</script>

<style>

</style>
<template>
    <UCard class="m-4">
        <h1 class="text-2xl font-bold mb-4">
            UI Elements
        </h1>
        <ul>
            <li>
                Blacklist editor
            </li>
            <li>
                Flagged User Inbox
            </li>
            <li>
                Test Endpoints
            </li>
            <li>
                Config UI Editor (After MVP)
            </li>
        </ul>
    </UCard>
    <UCard class="m-4">
        <h2 class="text-2xl font-bold mb-4">
            Flagged User Inbox
        </h2>
        <UTable :data="mockData"/>
    </UCard>
</template>

<script lang="ts" setup>
import { UTable } from '#components';

const mockData = reactive([
    {
        id: 1,
        username: "GlitchDev",
        flags: ['slurs'],
    }
])
</script>

<style scoped>

</style>
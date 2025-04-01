<template>
    <div class="p-4 flex gap-4 flex-col">
        <UCard>
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
        <UCard>
            <h2 class="text-2xl font-bold mb-4">
                Flagged User Inbox
            </h2>
            <UTable :data="mockData"/>
        </UCard>
    </div>
</template>

<script lang="ts" setup>
import { UTable } from '#components';
import { TITLE_SUFFIX } from '~/assets/data/appData';

useHead({
    title: 'Home' + TITLE_SUFFIX
})

const mockData = reactive([
    {
        id: 1,
        username: "GlitchDev",
        flags: ['slurs'],
    },
    {
        "id": 2,
        "username": "CodeNinja",
        "flags": ["spam", "harassment"]
    },
    {
        "id": 3,
        "username": "TechGuru",
        "flags": ["slurs"]
    },
    {
        "id": 4,
        "username": "User123",
        "flags": ["hate speech", "misinformation"]
    },
    {
        "id": 5,
        "username": "DevMaster",
        "flags": ["spam"]
    },
    {
        "id": 6,
        "username": "PixelArtist",
        "flags": ["harassment"]
    },
    {
        "id": 7,
        "username": "GamerPro",
        "flags": ["slurs", "hate speech"]
    },
    {
        "id": 8,
        "username": "WebWizard",
        "flags": ["misinformation"]
    },
    {
        "id": 9,
        "username": "DataDynamo",
        "flags": ["spam", "harassment"]
    },
    {
        "id": 10,
        "username": "CryptoQueen",
        "flags": ["scams"]
    },
    {
        "id": 11,
        "username": "DesignDiva",
        "flags": ["slurs"]
    },
    {
        "id": 12,
        "username": "MarketingMaven",
        "flags": ["misinformation", "spam"]
    },
    {
        "id": 13,
        "username": "AIWhiz",
        "flags": ["hate speech"]
    },
    {
        "id": 14,
        "username": "GameChanger",
        "flags": ["harassment", "slurs"]
    },
    {
        "id": 15,
        "username": "CodeCrafter",
        "flags": ["spam"]
    },
])
</script>

<style scoped>

</style>
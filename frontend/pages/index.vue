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
    </div>
</template>

<script lang="ts" setup>
import { UTable } from '#components';
import { TITLE_SUFFIX } from '~/assets/data/appData';

useHead({
    title: 'Home' + TITLE_SUFFIX
})
</script>

<style scoped>

</style>
<template>
    <ConfigLayout>
        <EndpointSummary
            path="scheduled pipeline" title="Pipeline Check"
            summary="This deep content check pipeline runs on a scheduled base to flag user content with a deep understanding."
        />
        <USwitch
            v-model="state.enabled"
            unchecked-icon="lucide-x"
            checked-icon="lucide-check"
            label="Endpoint enabled"
            size="xl" class="pb-8"
        />

        <!-- <div>
            <FeatureToggle
                v-model="state.check"
                title="Some Check"
                description="Placeholder description. Yoyoyo."
            />
        </div> -->
        <UButton label="Save" size="lg" class="mt-8" @click="submitConfig" />
    </ConfigLayout>
</template>

<script lang="ts" setup>
import type { ConfigBody } from '~/assets/types/pipeline';

const emit = defineEmits<{
    submit: [config: object, namespace: string]
}>();
const props = defineProps({
    config: {
        type: Object,
        required: true
    }
});

const state = reactive({
    enabled: true,
    // check: true
});

onBeforeMount(() => {
    Object.assign(state, props.config);
    // state.validFlags = props.config["blockedWords"].join(', ');
});

async function submitConfig() {
    const bodyState = { ...state } as ConfigBody;
    // bodyState.blockedWords = state.blockedWords.split(', ').map(s => s.trim()).filter(s => s.length > 0);

    emit("submit", bodyState, 'pipeline');
}
</script>

<style scoped></style>
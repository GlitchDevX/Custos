<template>
    <ConfigLayout>
        <EndpointSummary
            path="/check-content" title="Realtime Check"
            summary="This endpoint is serving metrics in the prometheus format." />
        <div>
            <USwitch
                v-model="state.enabled" unchecked-icon="lucide-x" checked-icon="lucide-check"
                label="Endpoint enabled" size="xl" class="pb-8" />
        </div>
        <UButton label="Save" size="lg" class="mt-8" @click="submitConfig" />
    </ConfigLayout>
</template>

<script lang="ts" setup>
import type { MetricsConfig } from '~/assets/types/config/metrics';

const emit = defineEmits<{
    submit: [config: MetricsConfig, namespace: string]
}>();
const props = defineProps({
    config: {
        type: Object as PropType<MetricsConfig>,
        required: true
    }
});

const state = reactive<MetricsConfig>({
    enabled: true
});

onBeforeMount(() => {
    Object.assign(state, props.config);
});

async function submitConfig() {
    emit("submit", state, 'metrics');
}
</script>

<style scoped></style>
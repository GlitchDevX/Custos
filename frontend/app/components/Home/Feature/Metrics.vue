<template>
    <div class="flex justify-center items-center">
        <div class="w-3xl max-w-full relative">
            <div class="max-w-xl">
                <h2 class="text-3xl font-bold flex flex-row gap-2 justify-start items-center">
                    Prometheus Metrics
                </h2>
                <p class="muted-text">
                    Exports prometheus metrics to easily monitor Custos out of the box.
                </p>
            </div>
            <div class="flex flex-col justify-end items-center pt-4 overflow-hidden">
                <div class="grow relative w-[505px] min-h-64">
                    <div>
                        <div
                            v-for="{ dotClass, lineClass} in positionDotLineClasses"
                            :key="'animation-metric-pos-dot-' + dotClass">
                            <div class="bg-neutral-800 w-1 rounded" :class="lineClass + ' ' + dotClass" />
                            <div class="bg-neutral-700 top-4 h-3 w-3 rounded-full" :class="dotClass" />
                            <div class="bg-neutral-700 top-4 h-3 w-3 rounded-full animate-ping" :class="dotClass" />
                        </div>
                        <div class="bg-error bottom-4 h-3 w-3 rounded-full absolute metric-pos-center-dot" />
                        <div class="bg-error bottom-4 h-3 w-3 rounded-full absolute animate-ping metric-pos-center-dot" />
                    </div>
                    <TransitionGroup name="animate-metric">
                        <UBadge
                            v-for="{ name, active, posClass } in metrics" v-show="active"
                            :key="'metric-animation-' + name" variant="subtle" size="lg"
                            class="absolute top-2" :class="posClass">
                            {{ name }}
                        </UBadge>
                    </TransitionGroup>
                </div>
                <NuxtImg
                    src="/prometheus_logo.png"
                    format="webp"
                    loading="lazy"
                    fetch-priority="low"
                    alt="Prometheus Logo"
                    class="rounded-2xl w-[50%]" />
            </div>
        </div>
    </div>
</template>

<script lang="ts" setup>
import { randomInt } from '~/assets/ts/math-utils';

const router = useRouter();

const metrics = ref([
    { name: "MAIL_OK", active: false, posClass: '' },
    { name: "MAIL_FORMAT_INVALID", active: false, posClass: '' },
    { name: "MAIL_DISPOSABLE", active: false, posClass: '' },
    { name: "MAIL_NO_SERVER", active: false, posClass: '' },
    { name: "MAIL_NO_ADDRESS", active: false, posClass: '' },
    { name: "MAIL_INVALID_DOMAIN", active: false, posClass: '' },
    { name: "MAIL_SMTP_DISCONNECT", active: false, posClass: '' },
    { name: "MAIL_SMTP_CONNECTION_ERROR", active: false, posClass: '' },
    { name: "MAIL_SMTP_TIMEOUT", active: false, posClass: '' },

    { name: "REALTIME_EXECUTED_CHECK", active: false, posClass: '' },
    { name: "REALTIME_URL_DETECTED", active: false, posClass: '' },
    { name: "REALTIME_BLOCKED_WORD_DETECTED", active: false, posClass: '' },

    { name: "ANALYZER_EXECUTED", active: false, posClass: '' },
    { name: "ANALYZER_TOXICITY_DETECTED", active: false, posClass: '' }
].sort(() => Math.random() - 0.5));

onMounted(() => {
    animateMetricsRec(0, 0);
});

const positions = ["metric-pos-left", "metric-pos-center", "metric-pos-right"]
const positionLineClasses = [
    "-rotate-30 translate-x-16.5 h-full",
    "translate-x-1 translate-y-4 h-[88%]",
    "rotate-30 -translate-x-14.5 h-full"
]
const positionDotLineClasses = positions.map((pos, index) => {
    return {
        dotClass: pos + '-dot',
        lineClass: positionLineClasses[index]
    }
});

async function animateMetricsRec(currentIndex: number, posCounter: number) {   
    const index = (currentIndex + 1) % metrics.value.length;
    const posIndex = (posCounter + 1) % positions.length;
    
    metrics.value[index]!.active = true;
    metrics.value[index]!.posClass = positions[posIndex]!;

    setTimeout(() => {
        metrics.value[index]!.active = false;
    }, 500);

    // user left page
    if (router.currentRoute.value.path !== "/") {
        return;
    }    

    const timeout = randomInt(500, 2000);
    requestAnimationFrame(() => {
        setTimeout(animateMetricsRec, timeout, index, posIndex);
    });
}
</script>

<style scoped>
.metric-pos-left {
    left: 25%;
    transform: translateX(-50%);
    position: absolute;
}
.metric-pos-center {
    left: 50%;
    transform: translateX(-50%);
    position: absolute;
}
.metric-pos-right {
    left: 75%;
    transform: translateX(-50%);
    position: absolute;
}

.metric-pos-left-dot {
    left: 25%;
    position: absolute;
}
.metric-pos-center-dot {
    left: 50%;
    position: absolute;
}
.metric-pos-right-dot {
    left: 75%;
    position: absolute;
}

.animate-metric-enter-active {
    transition: 0.3s;
}
.animate-metric-leave-active {
    transition: 5s ease-out;
}
.animate-metric-enter-from {
    opacity: 0;
}
.animate-metric-leave-to {
    top: 100%;
    left: 50% !important;
    transform: translateX(-50%);;
    opacity: 0;
}
</style>
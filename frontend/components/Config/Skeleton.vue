<template>
    <div>
        <USkeleton class="w-full h-10" />
        <div class="flex justify-center items-center">
            <div class="w-[800px]">
                <USkeleton class="w-64 h-7 mt-10" />
                <USkeleton class="w-2xl h-4 mt-2" />
                <div v-for="i in 5" :key="i">
                    <div class="flex flex-row gap-2 items-center mt-8">
                        <USkeleton class="w-11 h-8 rounded-full" />
                        <USkeleton class="w-64 h-4" />
                    </div>
                    <USkeleton class="w-xl h-4 mt-2" />
                </div>
                <USkeleton class="w-32 h-8 mt-8" />
            </div>
        </div>
    </div>
</template>

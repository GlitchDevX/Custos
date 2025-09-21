export const useBackend = () => {
    const baseUrl = "http://localhost:3060";

    async function validateMail(mail: string) {
        return await $fetch(`${baseUrl}/mail/`, {
            ignoreResponseError: true,
            method: 'post',
            body: { mail }
        });
    }

    async function getMetrics() {
        return await $fetch<string>(`${baseUrl}/metrics`, {
            ignoreResponseError: true,
            method: 'get',
        });
    }

    return { validateMail, getMetrics, url: baseUrl }
}
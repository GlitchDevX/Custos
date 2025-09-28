import type { AnalyzerResponse, ContentCheckResponse, MailValidationResponse, UpdateConfigResponse } from "~/assets/types/responses";
import type { NitroFetchOptions } from 'nitropack/types';
import type { BaseConfig } from "~/assets/types/configs";

export const useBackend = () => {
    const baseUrl = "http://localhost:3060";
    const defaultFetchOptions: Partial<NitroFetchOptions<any>> = {
        ignoreResponseError: true
    }

    async function validateMail(mail: string) {
        return await $fetch<MailValidationResponse>(`${baseUrl}/mail/`, {
            ...defaultFetchOptions,
            method: 'post',
            body: { mail }
        });
    }

    async function checkContent(content: string) {
        return await $fetch<ContentCheckResponse>(`${baseUrl}/content/`, {
            ...defaultFetchOptions,
            method: 'post',
            body: { content }
        });
    }

    async function executeAnalysis(content: string) {
        return await $fetch<AnalyzerResponse>(`${baseUrl}/analyze/`, {
            ...defaultFetchOptions,
            method: 'post',
            body: { content }
        });
    }

    async function getConfig<T extends BaseConfig>(namespace: string) {
        return await $fetch<T>(`${baseUrl}/config/`, {
            ...defaultFetchOptions,
            ignoreResponseError: false,
            method: 'get',
            query: { namespace }
        });
    }

    async function setConfig(namespace: string, content: object) {
        return await $fetch<UpdateConfigResponse>(`${baseUrl}/config/`, {
            ...defaultFetchOptions,
            method: 'put',
            body: { namespace, content }
        });
    }

    async function getMetrics() {
        return await $fetch<string>(`${baseUrl}/metrics`, {
            ...defaultFetchOptions,
            method: 'get',
        });
    }

    return { validateMail, checkContent, executeAnalysis, getConfig, setConfig, getMetrics, url: baseUrl }
}
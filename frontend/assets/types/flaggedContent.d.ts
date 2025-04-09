export type Tag = "profanity" | "spam" | "harassment" | "misinformation" | "other";
export type FlaggedUser = {reportId: string, userId: string, falseReport: boolean, flags: Tag[], content: string};
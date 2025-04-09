export type Tag = "slurs" | "spam" | "harassment" | "hate speech" | "misinformation" | "scams";
export type FlaggedUser = {reportId: string, userId: string, flags: Tag[], content: string};
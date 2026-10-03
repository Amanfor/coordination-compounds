import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const concepts = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/concepts" }),
  schema: z.object({
    title: z.string(),
    summary: z.string(),
    visual: z.string().optional(),
    order: z.number().optional(),
  }),
});

const questions = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/questions" }),
  schema: z.object({
    concept: z.string(),
    type: z.string(),
    difficulty: z.string(),
    options: z.array(z.string()).optional(),
    answer: z.string(),
    source: z.string().optional(),
  }),
});

export const collections = {
  concepts,
  questions,
};

import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "AI Exam Analyzer | Cognitive Level & Difficulty Engine",
  description:
    "AI-based automated question paper difficulty analyzer using NLP and revised Bloom's Taxonomy classification.",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}

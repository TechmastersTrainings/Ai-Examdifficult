import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "AI BASED AUTOMATIC QUESTION PAPER DIFFICULTY ANALYZER",
  description:
    "AI BASED AUTOMATIC QUESTION PAPER DIFFICULTY ANALYZER - Automated examination question paper difficulty and revised Bloom's Taxonomy cognitive demand evaluation platform.",
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

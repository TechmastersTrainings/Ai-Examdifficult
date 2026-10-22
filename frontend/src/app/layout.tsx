import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "CognitivePulse | Cognitive Level & Difficulty Engine",
  description:
    "Automated question paper difficulty analyzer using revised Bloom's Taxonomy classification.",
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

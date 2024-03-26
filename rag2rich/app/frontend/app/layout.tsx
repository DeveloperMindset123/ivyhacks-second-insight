import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";
import { Toaster } from "@/components/ui/sonner";
import { Header } from "@/components/header";
import { Providers } from "@/components/providers";
import { TailwindIndicator } from "@/components/tailwind-indicator";
import { cn } from "@/lib/utils";
import { GeistSans } from 'geist/font/sans'
import { GeistMono } from 'geist/font/mono'

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "secondInsight",
  description: "Get a second opinion",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body
        className={cn(
          'font-sans antialiased',
          GeistSans.variable,
          GeistMono.variable
        )}
      >
        <Toaster position="top-center" />
        <Providers
          attribute="class"
          defaultTheme="system"
          enableSystem
          disableTransitionOnChange
        >
            
            <main className="flex flex-col  background-gradient">
            
              {children}
              
            </main>
      
          <TailwindIndicator />
        </Providers>
      </body>
    </html>
  );
}

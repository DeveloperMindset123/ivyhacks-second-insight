"use client";  //will cause issues if this isn't added in regards to framer motion
import type { NextPage } from "next";
import Head from "next/head";
import Navbar from "../../components/Navbar";
import { motion } from "framer-motion";
import { riseWithFade, staggerChildren, videoAnimation, wordAnimation } from "../utils/animations";
import { Button } from "@/components/ui/button";
import Router from "next/router";
import Link from "next/link";
import { ContainerScroll } from "@/components/ui/container-scroll-animation";


export default function Home() {
    return (
      <><motion.div className="min-h-screen px-12 bg-white" initial="initial" animate="animate">
                <Head>
                    <title>Home | Second Insight</title>
                    <link rel="icon" href="/Users/ayandas/Desktop/VS_Code_Projects/ivyhacks-backend/rag2rich/app/frontend/app/assets/favicon.ico" />
                </Head>
                <Navbar />
                <main className="grid grid-cols-[3fr_1fr] py-10">
                    <h1 className="text-8xl font-bold w-[40rem] leading-[90%] tracking-[-2px] self-end">
                        <AnimatedWords title="An innovative AI stock advisor" />
                    </h1>
                    {/* <motion.div className="text-5xl w-6 leading-[150%]" variants={riseWithFade}>
      <Button>Lets go!</Button>
      </motion.div> */}
                </main>
                {/* <motion.video loop={true} autoPlay={true} muted={true} playsInline={true} variants={videoAnimation}>
        <source src=" " type="video/mp4"/>
    </motion.video> */}
                <><motion.div className="" variants={riseWithFade}>
                    <Link href={"/"}>
                        <Button className="text-5xl p-12"> Lets go!</Button>
                    </Link>
                </motion.div><footer className="flex justify-center text-sm text-zinc-400 py-12">
                        <p>&copy; 2022 Second Insight. All rights reserved.</p>
                    </footer></>
            </motion.div></>

    );
  }
  
  export const users = [
    {
      name: "Manu Arora",
      designation: "Founder, Algochurn",
      image: "https://picsum.photos/id/10/300/300",
      badge: "Mentor",
    },
    {
      name: "Sarah Singh",
      designation: "Founder, Sarah's Kitchen",
      image: "https://picsum.photos/id/11/300/300",
      badge: "Mentor",
    },
    {
      name: "John Doe",
      designation: "Software Engineer, Tech Corp",
      image: "https://picsum.photos/id/12/300/300",
      badge: "Mentor",
    },
    {
      name: "Jane Smith",
      designation: "Product Manager, Innovate Inc",
      image: "https://picsum.photos/id/13/300/300",
      badge: "Mentor",
    },
    {
      name: "Robert Johnson",
      designation: "Data Scientist, DataWorks",
      image: "https://picsum.photos/id/14/300/300",
      badge: "Mentor",
    },
    {
      name: "Emily Davis",
      designation: "UX Designer, DesignHub",
      image: "https://picsum.photos/id/15/300/300",
      badge: "Mentor",
    },
    {
      name: "Michael Miller",
      designation: "CTO, FutureTech",
      image: "https://picsum.photos/id/16/300/300",
      badge: "Mentor",
    },
    {
      name: "Sarah Brown",
      designation: "CEO, StartUp",
      image: "https://picsum.photos/id/17/300/300",
    },
    {
      name: "James Wilson",
      designation: "DevOps Engineer, CloudNet",
      image: "https://picsum.photos/id/18/300/300",
      badge: "Something",
    },
    {
      name: "Patricia Moore",
      designation: "Marketing Manager, MarketGrowth",
      image: "https://picsum.photos/id/19/300/300",
      badge: "Mentor",
    },
    {
      name: "Richard Taylor",
      designation: "Frontend Developer, WebSolutions",
      image: "https://picsum.photos/id/20/300/300",
    },
    {
      name: "Linda Anderson",
      designation: "Backend Developer, ServerSecure",
      image: "https://picsum.photos/id/21/300/300",
    },
    {
      name: "William Thomas",
      designation: "Full Stack Developer, FullStack",
      image: "https://picsum.photos/id/22/300/300",
      badge: "Badger",
    },
    {
      name: "Elizabeth Jackson",
      designation: "Project Manager, ProManage",
      image: "https://picsum.photos/id/23/300/300",
      badge: "Mentor",
    },
    {
      name: "David White",
      designation: "Database Administrator, DataSafe",
      image: "https://picsum.photos/id/24/300/300",
      badge: "Advocate",
    },
    {
      name: "Jennifer Harris",
      designation: "Network Engineer, NetConnect",
      image: "https://picsum.photos/id/25/300/300",
    },
    {
      name: "Charles Clark",
      designation: "Security Analyst, SecureIT",
      image: "https://picsum.photos/id/26/300/300",
    },
    {
      name: "Susan Lewis",
      designation: "Systems Analyst, SysAnalyse",
      image: "https://picsum.photos/id/27/300/300",
    },
    {
      name: "Joseph Young",
      designation: "Mobile Developer, AppDev",
      image: "https://picsum.photos/id/28/300/300",
      badge: "Mentor",
    },
    {
      name: "Margaret Hall",
      designation: "Quality Assurance, BugFree",
      image: "https://picsum.photos/id/29/300/300",
      badge: "Developer",
    },
  ];

type AnimatedWordsProps = {
  title: string;
};

const AnimatedWords : React.FC<AnimatedWordsProps> = ({title}) => {
    return (
        <motion.span variants={staggerChildren}>
            {title.split(" ").map((word, idx) => (
                <div key={idx} className="inline-block overflow-hidden">
                    <motion.span className="inline-block overflow-hidden" variants={wordAnimation}>{word + "\u00A0"}</motion.span>
                </div>
            ))}
        </motion.span>
    )
}

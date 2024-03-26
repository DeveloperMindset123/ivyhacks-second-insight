'use client'
import {Header} from "@/components/header";
import ChatSection from "../components/chat-section";
import { useState } from "react";
import { AnimatePresence, motion } from "framer-motion";
import ImageCollection from "@/components/loadingAnim";
// import Chat from "../components/chat";
export default function Home() {

  const [imagesLoading, setImagesLoading] = useState(true);

  return (
    <AnimatePresence mode="sync">
    {imagesLoading && (
      <motion.div key="imagesLoading">
        <ImageCollection
          setImagesLoading={(value:any) => setImagesLoading(value)}
        />
      </motion.div>
    )}
    {!imagesLoading && (
      <><Header /><div className="flex flex-row h-[100vh] overflow-hidden">
          <div className="pt-12 pr-4 pl-4  w-[18%] border-r shrink-0 bg-gradient-to-b from-background/90 via-background/50 to-background/10 backdrop-blur-xl">

            <h1 className="text-4xl font-bold">Chats</h1>
            <div className="flex flex-col mt-8 gap-2">
              <div className="w-full flex items-center h-12 bg-black rounded-3xl">
                <p className="text-white p-4 flex items-center text-md truncate">Risk management</p>
              </div>
              <div className="w-full flex items-center h-12 bg-white rounded-3xl">
                <p className="text-black p-4 flex items-center text-md truncate">Past assessment</p>
              </div>
              <div className="w-full flex items-center h-12 bg-white rounded-3xl">
                <p className="text-black p-4 flex items-center text-md truncate">Portfolio pred</p>
              </div>
            </div>
          </div>
          <ChatSection />
          <div className="pt-12 pr-8 pl-8  w-[25%] flex flex-col border-r shrink-0 bg-gradient-to-b from-background/90 via-background/50 to-background/10 backdrop-blur-xl">
            <div className="flex flex-row gap-2 w-full justify-between">
              <p className="underline-offset-4 underline text-blue-500">Media</p>
              <p className="underline-offset-4 underline">Links</p>
              <p className="underline-offset-4 underline">Docs</p>
            </div>
            <div className="flex flex-row mt-8 gap-4 shrink-0 justify-center">
              <img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Farizent.brightspotcdn.com%2Fdims4%2Fdefault%2Ffca4cb4%2F2147483647%2Fstrip%2Ftrue%2Fcrop%2F646x384%2B0%2B0%2Fresize%2F646x384!%2Fquality%2F90%2F%3Furl%3Dhttps%3A%252F%252Farizent.brightspotcdn.com%252F7a%252F79%252F325892ce45a286402aa4f73e3d46%252F10q.jpg&f=1&nofb=1&ipt=3502f7328e1e30b3c170bd59f2f93435a7e24276838fc131902935663d83f216&ipo=images" className=" w-[5.3rem] rounded-xl h-20"></img>
              <img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.investopedia.com%2Finv%2Farticles%2Fslideshow%2Fsec-filings-forms%2Freading-the-sec-forms.jpg%3Fquality%3D80%26width%3D680%26height%3D680&f=1&nofb=1&ipt=6e2a60afa621e5ae1609ca85525c4287daa17c43f2e0d74d6ea3582c2375ca94&ipo=images" className=" w-[5.3rem] rounded-xl h-20"></img>
              <img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fcorporatefinanceinstitute.com%2Fassets%2Fsec-form-10k-600x261.png&f=1&nofb=1&ipt=4c825482c4905efb27637f38e957c57a56a221e80f7a1832afe23b61fd5006d3&ipo=images" className=" w-[5.3rem] rounded-xl h-20"></img>
            </div>
          </div>
        </div></>
    )}
  </AnimatePresence>
    
      // <Chat user={null} secret={null} />
  );
}

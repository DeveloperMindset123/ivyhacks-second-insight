import { Loader2 } from "lucide-react";
import { useEffect, useRef } from "react";

import ChatActions from "./chat-actions";
import ChatMessage from "./chat-message";
import { ChatHandler } from "./chat.interface";

export default function ChatMessages(
  props: Pick<ChatHandler, "messages" | "isLoading" | "reload" | "stop">,
) {

  const scrollableChatContainerRef = useRef<HTMLDivElement>(null);
  const messageLength = props.messages.length;
  const lastMessage = props.messages[messageLength - 1];

  const scrollToBottom = () => {
    if (scrollableChatContainerRef.current) {
      scrollableChatContainerRef.current.scrollTop =
        scrollableChatContainerRef.current.scrollHeight;
    }
  };

  const isLastMessageFromAssistant =
    messageLength > 0 && lastMessage?.role !== "user";
  const showReload =
    props.reload && !props.isLoading && isLastMessageFromAssistant;
  const showStop = props.stop && props.isLoading;

  // `isPending` indicate
  // that stream response is not yet received from the server,
  // so we show a loading indicator to give a better UX.
  const isPending = props.isLoading && !isLastMessageFromAssistant;

  useEffect(() => {
    scrollToBottom();
  }, [messageLength, lastMessage]);

  return (
<div className="w-full h-[80%]  border-r shrink-0 bg-gradient-to-b from-background/50 via-background/70 to-background/90 backdrop-blur-xl p-4 pb-0 relative">
  <div className="absolute inset-0 bg-gradient-to-b from-background/90 via-background/70 to-background/50"></div>
      <div
        className="flex h-[50vh] flex-col gap-5 relative z-10 divide-y overflow-y-auto pb-4"
        ref={scrollableChatContainerRef}
      >
        {props.messages.map((m) => (
          <ChatMessage key={m.id} {...m} />
        ))}
        {isPending && (
          <div className="flex justify-center items-center pt-10">
            <Loader2 className="h-4 w-4 animate-spin" />
          </div>
        )}
      </div>
      <div className="flex relative z-10 justify-end py-4">
        <ChatActions
          reload={props.reload}
          stop={props.stop}
          showReload={showReload}
          showStop={showStop}
        />
      </div>
      {props.messages.length == 0  && (
        <div className="w-full gap-4  flex-wrap h-[10rem]  mb-[10rem] shrink-0 rounded-xl flex flex-row justify-center items-center">
        <div className="flex flex-row w-full mb-[2rem] flex-wrap gap-4">
        <div className="w-[48.5%]  transition h-20 rounded-lg flex flex-col cursor-pointer justify-center px-4 truncate bg-white border relative z-10">
          <h2 className="font-bold text-black 0 -mb-1">What is my risk</h2>
          <p className="text-gray-700">if I invest $1000 in Berkshire in 2024?</p>
        </div>
        <div className="w-[48.5%] h-20 rounded-lg flex flex-col cursor-pointer justify-center px-4 truncate bg-white border relative z-10">
          <h2 className="font-bold !text-black 0 -mb-1">Give me a visualization</h2>
          <p className="text-gray-700">about for my portfolio.</p>
        </div>

        <div className="w-[48.5%] h-20 rounded-lg flex flex-col cursor-pointer justify-center px-4 truncate bg-white border relative z-10">
          <h2 className="font-bold !text-black 0 -mb-1">Present risk for my vc investments</h2>
          <p className="text-gray-700">critique it as well!</p>
        </div>
        <div className="w-[48.5%] h-20 rounded-lg flex flex-col cursor-pointer justify-center px-4 truncate bg-white border relative z-10">
          <h2 className="font-bold !text-black 0 -mb-1">Provide another insight</h2>
          <p className="text-gray-700">on my provided files.</p>
        </div>
        </div>
      </div>
      )}
      
</div>
  );
}

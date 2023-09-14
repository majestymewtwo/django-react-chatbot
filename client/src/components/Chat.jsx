import React from "react";
import bot from "/bot.png";
import user from "/user.png";

export const Chat = React.forwardRef(({ type, message }, ref) => {
  return (
    <div
      ref={ref}
      className={`flex ${
        type === "bot" ? "flex-row" : "flex-row-reverse"
      } mb-2 w-full`}>
      <div
        className={`flex ${
          type === "bot" ? "justify-start" : "justify-end"
        } w-fit max-w-[45%] py-2 px-4 items-center space-x-3 rounded-2xl bg-gradient-to-br from-[#016A70] to-[#183D3D] text-white`}>
        <img
          src={type === "user" ? user : bot}
          className='h-10 w-10 rounded-full'
          alt='pfp'
        />
        <p className='text-sm'>{message}</p>
      </div>
    </div>
  );
});

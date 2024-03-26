import Image from 'next/image';
import { motion } from 'framer-motion';

const staggerChildren = {
  show: {
    transition: {
      staggerChildren: 0.55,
    },
  },
};

const staggerAnimations = {
  hidden: { opacity: 0, y: 200, scale: 0.75 },
  show: {
    opacity: 1,
    y: 0,
    scale: 1,
    transition: {
      ease: [0.6, 0.01, 0.35, 0.95],
      duration: 1.4,
    },
  },
  exit: {
    opacity: 0,
    y: -200,
    transition: {
      ease: 'easeInOut',
      duration: 0.8,
    },
  },
};

const mainImg = {
  hidden: { opacity: 0, y: 200 },
  show: {
    opacity: 1,
    y: 0,
    transition: {
      ease: [0.6, 0.01, 0.35, 0.95],
      duration: 1.6,
    },
  },
};

export default function ImageCollection({ setImagesLoading }: any) {
    return (
      <motion.div
        className="absolute w-screen h-screen flex items-center justify-center"
        variants={staggerChildren}
        onAnimationComplete={() => setImagesLoading(false)}
        initial="hidden"
        animate="show"
        exit="exit"
      >
        <motion.div variants={staggerAnimations} className="absolute w-[400px] object-fill left-16 bottom-14">
          <Image src="/fin.jpg" alt="" width={400} height={400} />
        </motion.div>
        <motion.div variants={mainImg} className="absolute object-fill w-[800px]">
          <Image src="/graph.jpg" alt="" width={800} height={800} layout="responsive" />
        </motion.div>
        <motion.div variants={staggerAnimations} className="absolute object-fill w-[300px] right-12 top-8">
          <Image src="/businesman.jpg" alt="" width={300} height={300} layout="responsive" />
        </motion.div>
        <motion.div variants={staggerAnimations} className="absolute object-fill w-[400px] right-20 bottom-10">
          <Image src="/risk.jpg" alt="" width={400} height={300} />
        </motion.div>
        <motion.div variants={staggerAnimations} className="absolute object-fill w-[280px] left-14 top-12">
          <Image src="/braine.jpg" alt="" width={400} height={300} />
        </motion.div>
      </motion.div>
    );
  }
  
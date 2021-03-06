from Contra import env_contra
import tqdm

from Contra.env_contra import ContraEnv

env = ContraEnv()

done = True

try:
    for _ in tqdm.tqdm(range(5000)):
        if done:
            state = env.reset()
            done = False
        else:
            state, reward, done, info = env.step(env.action_space.sample())
except KeyboardInterrupt:
    pass

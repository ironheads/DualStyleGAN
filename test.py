from model.stylegan.model import Generator, Discriminator

if __name__=='__main__':
    model = Generator(1024,512,8)
    print(model)
    print(model.module)
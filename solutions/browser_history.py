class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = homepage
        self.history = [homepage]
        self.curr_index = 0

    def visit(self, url: str) -> None:
        self.history = self.history[:self.curr_index+1]
        self.history.append(url)
        self.curr_index += 1

    def back(self, steps: int) -> str:
        self.curr_index = max(self.curr_index - steps, 0)

        return self.history[self.curr_index]

    def forward(self, steps: int) -> str:
        #if steps > (len(self.history) - 1)- self.curr_index:
         #   self.curr_index = 
          #  return self.history[-1]

        #while steps > 0:
        #   steps -= 1
        #   self.curr_index += 1
        self.curr_index = min(self.curr_index + steps, len(self.history) -1)
        #minimum b/w the index wanted, and if it's more than higory it returns the last element
        
        return self.history[self.curr_index]
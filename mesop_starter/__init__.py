import mesop as me 

@me.stateclass
class State:
    count : int 

@me.page(path = "/hello_world")
def app():
    me.text("Hello World")

def button_click(event : me.ClickEvent):
    state = me.state(State)
    state.count += 1
    
@me.page(path="/counter")
def counter():
    state = me.state(State)
    me.button("Increment", on_click = button_click)
    me.text("Counter:{0}".format(state.count))
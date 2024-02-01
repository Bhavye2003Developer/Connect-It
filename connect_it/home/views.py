import keyboard
from django.shortcuts import render, redirect
from pynput.mouse import Button, Controller
import mouse

mouseController = Controller()


def home(request):
    return render(request, "home/index.html")


def enter(request):
    mouse.click('left')
    return redirect("home")


def ScrollDown(request):
    mouseController.scroll(0, -3)
    return redirect("home")


def ScrollUp(request):
    mouseController.scroll(0, 3)
    return redirect("home")


def up(request):
    current_mouse_position = mouseController.position
    print(current_mouse_position)
    mouse.move(0, -30, absolute=False, duration=0.2)
    return redirect("home")


def down(request):
    current_mouse_position = mouseController.position
    print(current_mouse_position)
    mouse.move(0, 30, absolute=False, duration=0.2)
    return redirect("home")


def left(request):
    current_mouse_position = mouseController.position
    print(current_mouse_position)
    mouse.move(-30, 0, absolute=False, duration=0.2)
    return redirect("home")


def right(request):
    current_mouse_position = mouseController.position
    print(current_mouse_position)
    mouse.move(30, 0, absolute=False, duration=0.2)
    return redirect("home")


def write(request):
    if (request.method == "POST"):
        content = request.POST.get("content")
        isEntered = request.POST.get("Enter")
        print(content, isEntered)

        # keyboard.press_and_release('ctrl+a, ctrl+alt+del')
        keyboard.write(content)
        if (isEntered):
            keyboard.press_and_release('enter')

    return redirect("home")

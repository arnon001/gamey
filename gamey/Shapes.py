# # Draw
# class Draw(Screen):
#     # drawing a rectangle
#     def rect(x=0, y=0, w=100, h=100, color=(255, 255, 255)):
#         goomy.draw.rect(Screen.screen, color, [x, y, w, h])

#     # drawing a circle
#     def circle(x=0, y=0, radius=30, color=(255, 255, 255)):
#         goomy.draw.circle(Screen.screen, color, (x, y), radius)

#     # drawing a elipse
#     def elipse(x=0, y=0, w=100, h=50, color=(255, 255, 255)):
#         rect = goomy.Rect((x, y), (w, h))
#         goomy.draw.ellipse(Screen.screen, color, rect)

#     # drawing a line
#     def line(x_start=10, y_start=10, x_end=380, y_end=380, color=(255, 255, 255), width=1):
#         goomy.draw.line(Screen.screen, color,
#                         (x_start, y_start), (x_end, y_end), width=width)
import sys
import pygame

pygame.init()
pygame.display.set_caption('Real estate tycoon')
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
grey = (50, 50, 50)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

font_large = pygame.font.SysFont("AgencyFB", 40)
font_medium = pygame.font.SysFont("AgencyFB", 25)
font_small = pygame.font.SysFont("AgencyFB", 15)

clock = pygame.time.Clock()
game_speed = 60


class Game:
    def __init__(self):
        self.money = 0
        self.shops = 0
        self.houses = 0
        self.mansions = 0
        self.income = 0
        self.income_timer = 6.0
        self.game_running = True
        print("Game successfully initialized")

    def game_status(self):
        player_cash_text = font_large.render("Money:", True, white)
        screen.blit(player_cash_text, [340, 20])
        player_cash_amount = font_large.render(str(self.money), True, green)
        screen.blit(player_cash_amount, [440, 20])

        player_income_text = font_medium.render("Income (/min):", True, white)
        screen.blit(player_income_text, [340, 80])
        player_income_value = font_medium.render(str(self.income), True, green)
        screen.blit(player_income_value, [465, 80])
        player_income_value = font_small.render("Yields money every 6 seconds", True, green)
        screen.blit(player_income_value, [360, 110])

        # Progress bar:
        pygame.draw.rect(screen, grey, [530, 85, 100, 20])
        pygame.draw.rect(screen, black, [533, 88, 94, 14])
        pygame.draw.rect(screen, blue, [533, 88, (self.income_timer/6.0) * 94, 14])

        work_text = font_medium.render("[W] Work a shift", True, white)
        screen.blit(work_text, [340, 140])
        work_tip = font_small.render(f"No costs, yields {Shift.income_once}, {Shift.build_time} sec to complete", True, red)
        screen.blit(work_tip, [360, 170])

        player_shops_text = font_medium.render("[S] Build a shop to let", True, white)
        screen.blit(player_shops_text, [340, 210])
        player_shops_value = font_medium.render(str(self.shops), True, yellow)
        screen.blit(player_shops_value, [560, 210])
        shop_tip = font_small.render(f"Costs {Shop.cost}, yields {Shop.income_per_min}/minute, {Shop.build_time} sec to complete", True, red)
        screen.blit(shop_tip, [360, 240])

        player_houses_text = font_medium.render("[H] Build a house to let", True, white)
        screen.blit(player_houses_text, [340, 280])
        player_houses_value = font_medium.render(str(self.houses), True, yellow)
        screen.blit(player_houses_value, [560, 280])
        house_tip = font_small.render(f"Costs {House.cost}, yields {House.income_per_min}/minute, {House.build_time} sec to complete", True, red)
        screen.blit(house_tip, [360, 310])

        player_houses_text = font_medium.render("[M] Build a mansion to let", True, white)
        screen.blit(player_houses_text, [340, 350])
        player_houses_value = font_medium.render(str(self.mansions), True, yellow)
        screen.blit(player_houses_value, [560, 350])
        mansion_tip = font_small.render(f"Costs {Mansion.cost}, yields {Mansion.income_per_min}/minute, {Mansion.build_time} sec to complete", True, red)
        screen.blit(mansion_tip, [360, 380])

        delete_job_text = font_medium.render("[R] Remove the last job", True, white)
        screen.blit(delete_job_text, [340, 420])

    def generate_income(self):
        if self.income_timer > 0:
            self.income_timer -= 1/game_speed
        else:
            self.income_timer = 6.0
            self.money += int(self.income / 5)

    def ret_game(self):
        print("Game starting")
        while self.game_running:
            self.input_event_handling()
            job_queue.progress_project()
            self.generate_income()
            if len(job_queue.queue) > 0:
                completion = job_queue.construction_timer / job_queue.queue[0].build_time
            else:
                completion = 0

            screen.fill(black)
            job_queue.draw_queue(completion)
            self.game_status()

            pygame.display.update()
            clock.tick(game_speed)

    def input_event_handling(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.game_running = False
                elif event.key == pygame.K_w:
                    job_queue.enqueue(Shift)
                elif event.key == pygame.K_s:
                    if self.money >= Shop.cost:
                        self.money -= Shop.cost
                        job_queue.enqueue(Shop)
                elif event.key == pygame.K_h:
                    if self.money >= House.cost:
                        self.money -= House.cost
                        job_queue.enqueue(House)
                elif event.key == pygame.K_m:
                    if self.money >= Mansion.cost:
                        self.money -= Mansion.cost
                        job_queue.enqueue(Mansion)
                elif event.key == pygame.K_c:
                    if len(job_queue.queue) > 0:
                        self.money += job_queue.queue[0].cost
                        job_queue.working = False
                    job_queue.dequeue()
                elif event.key == pygame.K_r:
                    if len(job_queue.queue) > 0:
                        self.money += job_queue.queue[-1].cost
                        if len(job_queue.queue) == 1:
                            job_queue.working = False
                    job_queue.remove_last()


class JobQueue:
    def __init__(self):
        self.queue = []
        self.working = False
        self.construction_timer = 0

    def enqueue(self, item):
        if len(self.queue) < 5:
            self.queue.append(item)

    def dequeue(self):
        self.queue.pop(0)

    def remove_last(self):
        self.queue.pop(-1)

    def progress_project(self):
        if not self.working:
            self.new_project()
        elif self.working:
            if self.construction_timer <= 0:
                self.project_completed()
            else:
                self.construction_timer -= 1/game_speed

    def new_project(self):
        if len(self.queue) > 0:
            self.construction_timer = self.queue[0].build_time
            self.working = True

    def project_completed(self):
        self.working = False
        self.queue[0].project_done()
        self.dequeue()

    def draw_queue(self, progress):
        pygame.draw.rect(screen, grey, [20, 20, 300, 80])
        current_job_text = font_medium.render("Current job:", True, white)
        screen.blit(current_job_text, [20, 20])
        if len(self.queue) > 0:
            current_job_type = font_medium.render(self.queue[0].type, True, green)
        else:
            current_job_type = font_medium.render("EMPTY", True, red)
        screen.blit(current_job_type, [130, 40])
        c_to_cancel_text = font_small.render("Press C to cancel", True, white)
        screen.blit(c_to_cancel_text, [230, 80])

        # Progress bar:
        pygame.draw.rect(screen, black, [210, 50, 100, 20])
        pygame.draw.rect(screen, red, [213, 53, 94, 14])
        pygame.draw.rect(screen, green, [213, 53, progress * 94, 14])

        pygame.draw.rect(screen, grey, [20, 110, 200, 80])
        queue1_text = font_medium.render("Queued 1:", True, white)
        screen.blit(queue1_text, [20, 110])
        if len(self.queue) > 1:
            queue1_type = font_medium.render(self.queue[1].type, True, green)
        else:
            queue1_type = font_medium.render("EMPTY", True, red)
        screen.blit(queue1_type, [130, 130])

        pygame.draw.rect(screen, grey, [20, 200, 200, 80])
        queue2_text = font_medium.render("Queued 2:", True, white)
        screen.blit(queue2_text, [20, 200])
        if len(self.queue) > 2:
            queue2_type = font_medium.render(self.queue[2].type, True, green)
        else:
            queue2_type = font_medium.render("EMPTY", True, red)
        screen.blit(queue2_type, [130, 220])

        pygame.draw.rect(screen, grey, [20, 290, 200, 80])
        queue3_text = font_medium.render("Queued 3:", True, white)
        screen.blit(queue3_text, [20, 290])
        if len(self.queue) > 3:
            queue3_type = font_medium.render(self.queue[3].type, True, green)
        else:
            queue3_type = font_medium.render("EMPTY", True, red)
        screen.blit(queue3_type, [130, 310])

        pygame.draw.rect(screen, grey, [20, 380, 200, 80])
        queue4_text = font_medium.render("Queued 4:", True, white)
        screen.blit(queue4_text, [20, 380])
        if len(self.queue) > 4:
            queue4_type = font_medium.render(self.queue[4].type, True, green)
        else:
            queue4_type = font_medium.render("EMPTY", True, red)
        screen.blit(queue4_type, [130, 410])


class Job:
    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.__class__.__name__


class Shift(Job):
    type = "Work"
    status = 'Shift'
    cost = 0
    build_time = 3
    income_per_min = 0
    income_once = 15

    @staticmethod
    def project_done():
        game.money += Shift.income_once


class Shop(Job):
    type = "Shop"
    status = 'Shop construction'
    cost = 50
    build_time = 6
    income_per_min = 20
    income_once = 0

    @staticmethod
    def project_done():
        game.income += Shop.income_per_min
        game.shops += 1


class House(Job):
    type = "House"
    status = 'House construction'
    cost = 500
    build_time = 17
    income_per_min = 200
    income_once = 0

    @staticmethod
    def project_done():
        game.income += House.income_per_min
        game.houses += 1


class Mansion(Job):
    type = "Mansion"
    status = 'Mansion construction'
    cost = 5000
    build_time = 45
    income_per_min = 2000
    income_once = 0

    @staticmethod
    def project_done():
        game.income += Mansion.income_per_min
        game.mansions += 1


if __name__ == '__main__':
    game = Game()
    job_queue = JobQueue()
    game.ret_game()

    sys.exit(0)

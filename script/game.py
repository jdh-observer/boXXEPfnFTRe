import random
import sys

from csv_parser import read_csv
from statistics import PlayerStatistics

random.seed()

positions = read_csv("data/positions.csv", "PosID,ranktrad,rankint,Name,Type,Department,Location,Remarks".split(","))
commissions = read_csv("data/commissions.csv", "PosID,Name,Type,Department,Location,virtuous,talented,garland,meritorious,good,weak,corrupt".split(","))
performance = read_csv("data/performance.csv", "PosID,Name,Type,Department,Location,virtuous,talented,garland,meritorious,good,weak,corrupt".split(","))
honorific = read_csv("data/honorific.csv", "PosID,ranktrad,rankint,Name,Type,Department,Location,pool,player,Remarks".split(","))
uniquerels = read_csv("data/uniquerels.csv", "SourceID,Dice,TargetID,pool,player,Remarks".split(","))
comperfrels1 = read_csv("data/comperfrels1.csv", "SourceID,Dice,TargetID,Target,pool,player,".split(","))
comperfrels2 = read_csv("data/comperfrels2.csv", "SourceID,Source,Dice,TargetID,Target,pool,player,Remarks".split(","))
comperfrels2a = read_csv("data/comperfrels2a.csv", "SourceID,Source,Dice,TargetID,Target,pool,player,Remarks".split(","))
comperfrels3 = read_csv("data/comperfrels3.csv", "SourceID,Source,Dice,TargetID,pool,player,Remarks,".split(","))
luckyrels0 = read_csv("data/luckyrels0.csv", "SourceID,Dice,TargetID,pool,player,Remarks".split(","))
luckyrels1 = read_csv("data/luckyrels1.csv", "SourceID,Dice,TargetID,Target,pool,player,Remarks".split(","))
luckyrels2 = read_csv("data/luckyrels2.csv", "SourceID,Source,Dice,TargetID,Target,pool,player,Remarks".split(","))
luckyrels3 = read_csv("data/luckyrels3.csv", "SourceID,Source,Dice,TargetID,pool,player,Remarks".split(","))
purchaserels = read_csv("data/purchaserels.csv", "Source,Dice,Target,pool,player,Remarks".split(","))


""" Moving to 協辦 is only permitted for people with a certain background,
	i.e. players having visited certain fields in the game. To model this,
	we need special rules in a few places, so we enumerate all positions
	that can move to 協辦 when rolling 德 here. """
xieban_origin_positions = ["C28-督院：P175-總督", "C32-工部：P190-尚書", "C33-刑部：P198-尚書", "C34-兵部：P206-尚書", "C35-禮部：P213-尚書",
	"C36-戶部：P223-尚書", "C37-吏部：P231-尚書"]

""" Moving to 御史 from 郎中 and 員外 positions is only permitted with a
    certain background, so again enumerate the positions this applies 
    to. """
yushi_origin_positions = ["C32-工部：P193-郎中",  "C32-工部：P194-員外", "C33-刑部：P201-郎中", "C33-刑部：P202-員外",
	"C34-兵部：P210-員外", "C35-禮部：P216-郎中", "C35-禮部：P217-員外", "C37-吏部：P234-郎中",  "C37-吏部：P235-員外"]

""" Similarily, moving to 總裁, 主考 and 同考 is also restricted. """
zongcai_origin_positions = ["C32-工部：P191-左侍郎", "C32-工部：P193-郎中",  "C32-工部：P195-主事", "C33-刑部：P202-員外",
	"C33-刑部：P203-主事", "C34-兵部：P206-尚書", "C34-兵部：P210-員外", "C34-兵部：P211-主事",
	"C35-禮部：P213-尚書", "C35-禮部：P216-郎中", "C35-禮部：P218-主事", "C37-吏部：P231-尚書",
	"C37-吏部：P232-左侍郎", "C15-縣：P93-煩縣", "C15-縣：P94-簡縣"]

""" The player has agency to refuse a moves leading to 謄錄 and 教習.
	If they do so, they remain in their previous position. """
refusable_moves = [("C1-出身：P3-貢生", "良"), ("C1-出身：P3-貢生", "柔"),
	("C3-學院：P27-拔貢", "柔"), ("C3-學院：P29-恩貢", "柔"),
	("C3-學院：P30-歲貢", "柔"), ("C4-鄉試：P38-經魁", "柔"),
	("C4-鄉試：P39-舉人", "柔"), ("C4-鄉試：P40-副榜", "良")]

assert(commissions[0].keys() == performance[0].keys())
comperf = commissions + performance

assert(comperfrels2[0].keys() == comperfrels2a[0].keys())
#TODO: What is the purpose of comperfrels2a? It seems to duplicate
# relations also present in comperfrels2
# comperfrels2.extend(comperfrels2a)

def print_game_state(s):
	#print(s)
	return

print_game_state(f"Successfully loaded {len(positions)} regular positions, {len(commissions)} commission positions, {len(performance)} performance positions, {len(honorific)} honorific positions")
print_game_state(f"Also loaded {len(uniquerels)} unique relations, {len(comperfrels1)} comperfrels1, {len(comperfrels2)} comperfrels2 (including 2a), {len(comperfrels3)} comperfrels3, {len(luckyrels0)} lucky relations 0, {len(luckyrels1)} lucky relations 1, {len(luckyrels2)} lucky relations 2, {len(luckyrels3)} lucky relations 3, {len(purchaserels)} purchase relations")

""" Office purchase strategies. """

""" Strategy that never buys an office. """
class NeverPurchaseStrategy:
	def __call__(self, game, player):
		return None

""" Strategy that buys an office with fixed probability. When it decides
	to buy, it will pick at random one of the offices available. """
class RandomPurchaseStrategy:
	def __init__(self, purchase_probability):
		self.purchase_probability = purchase_probability
	
	def __call__(self, game, player):
		""" random.random() returns a uniformely distributed float with 0 <= X < 1.0 """
		if random.random() < self.purchase_probability:
			options = player.get_potential_purchase_targets()
			if options != []:
				return random.choice(options)
			else:
				return None
		else:
			return None

""" Strategy that buys office if player still has a low rank after a
	certain number of dice rolls. """
class LatePurchaseStrategy:
	def __init__(self, rolls, rank):
		self.rolls = rolls
		self.rank = rank
	
	def __call__(self, game, player):
		if player.statistics.should_have_purchased_office == 1:
			return None
		
		if player.statistics.num_dice_rolls >= self.rolls and (not player.is_ranked() or player.rankint < self.rank):
			if player.get_position_props()["Type"] == "Exam":
				player.statistics.was_in_exam_when_purchase_strategy_applied = 1
			options = player.get_potential_purchase_targets()
			if options != []:
				if not player.statistics.has_purchased_office and random.random() < 0.5:
					player.statistics.should_have_purchased_office = 1
					return None
				else:
					return random.choice(options)

""" Strategy that buys office if player is the last and n ranks behind
	second worst. """
class CatchUpPurchaseStrategy:
	def __init__(self, n):
		self.n = n
	
	def __call__(self, game, player):
		if player.statistics.should_have_purchased_office == 1:
			return None
		
		my_rankint = player.rankint if player.is_ranked() else 0
		others_rankint = [q.rankint if q.is_ranked() else 0 for q in game.players if q != player]
		if min(others_rankint) - my_rankint >= self.n:
			options = player.get_potential_purchase_targets()
			if player.get_position_props()["Type"] == "Exam":
				player.statistics.was_in_exam_when_purchase_strategy_applied = 1
			if options != []:
				if not player.statistics.has_purchased_office and random.random() < 0.5:
					player.statistics.should_have_purchased_office = 1
					return None
				else:
					return random.choice(options)

""" Class that models the state of a player. """
class Player:
	def __init__(self, purchase_strategy = NeverPurchaseStrategy()):
		self._position = "C0-局外：P0-白丁" 
		self._secondary_position = None
		
		self.statistics = PlayerStatistics()
		
		""" Amount of money that has been paid out to this player from the
			pool over the course of the game so far. """
		self.money_from_pool = 0
		
		""" Amount of money that the player has paid out to the pool so far. """
		self.money_to_pool = 0
		
		""" Amount of money that the player has received from other players
			over the course of the game so far. """
		self.money_from_players = 0
		
		""" Amount of money that the player had to pay to other players so far."""
		self.money_to_players = 0
		
		""" Boolean that is True if the player, via the positions they 
			have visited so far, is Manchu. """
		self.is_manchu = False
		
		""" Boolean that is True if the player has passed through the 
		    Hanlin yuan. """
		self.is_hanlin = False
		
		""" Booleans that are True if the player has ever held the 舉人
			position / 進士 position respectivly. """
		self.is_juren = False
		self.is_jinshi = False
		
		""" Boolean that is True if the player passed through the 
			捐班 system. """
		self.is_juanban = False
		
		""" In the "太醫院" and the "欽天監" the player can rise in rank
			while staying at the same field. This is variable is used 
			to capture that. """
		self._special_rankint = None
		
		""" Strategy that is used to determine whether the player should
			buy an office. """
		self.purchase_strategy = purchase_strategy
	
	""" Returns True iff the player has not yet entered the gameboard,
		i.e. is in the position "C0-局外：P0-白丁" """
	def is_outside_board(self):
		return self.position == "C0-局外：P0-白丁"
	
	""" Position ID of the primary token of the player. """
	@property
	def position(self):
		return self._position
	
	@position.setter
	def position(self, new_position):
		old_position_rankint = self.get_position_props()["rankint"]
		self._position = new_position
		
		self.statistics.num_moves_to_new_position += 1
		if self.statistics.first_position is None:
			self.statistics.first_position = new_position
		self.statistics.positions_visit_counter[next(i for i, p in enumerate(positions) if p["PosID"] == new_position)] += 1
		
		""" There are a few position passing through which can affect
			later events in the game, so we record those here. """
		if "C56-翰林院" in new_position:
			if not self.is_hanlin:
				print_game_state("Obtained status as Hanlin member.")
				self.is_hanlin = True
		if new_position == "C4-鄉試：P39-舉人":
			if not self.is_juren:
				print_game_state("Obtained status as 舉人.")
				self.is_juren = True
		if new_position == "C5-會試：P46-進士":
			if not self.is_jinshi:
				print_game_state("Obtained status as 進士.")
				self.is_jinshi = True
		if "C14-捐班候補" in new_position:
			if not self.is_juanban:
				print_game_state("Obtained status as 捐班.")
				self.is_juanban = True
		if new_position in ("C1-出身：P7-筆帖式", "C1-出身：P12-官學生") or "滿缺" in new_position:
			if not self.is_manchu:
				print_game_state("Obtained status as Manchu.")
				self.is_manchu = True
		if next(p for p in positions if p["PosID"] == new_position)["Type"] == "Exam":
			self.statistics.has_visited_exam = 1
		
		if ("C39-太醫院" in new_position or "C40-欽天監" in new_position) and self.is_ranked():
			if self._special_rankint is None:
				self._special_rankint = self.rankint
			else:
				""" When moving in these two boards while already having
					a special rank assigned, update the rank by the delta
					of the two positions."""
				self._special_rankint += self.get_position_props()["rankint"] - old_position_rankint
		else:
			self._special_rankint = None
		
		assert(len(list(p for p in positions if p["PosID"] == new_position)) == 1)
	
	def get_position_props(self):
		return next((p for p in positions if p["PosID"] == self.position))
	
	@property
	def rankint(self):
		assert(self.is_ranked())
		if self._special_rankint:
			return self._special_rankint
		else:
			return self.get_position_props()["rankint"]
	
	def increase_special_rankint(self, x):
		assert(self._special_rankint is not None)
		self._special_rankint += x
	
	@property
	def ranktrad(self):
		assert(self.is_ranked())
		return self.get_position_props()["ranktrad"]
	
	""" Position ID of the secondary token (used for commissions,
			performance and honrifics). None if secondary token
			is not in the game. """
	@property
	def secondary_position(self):
		return self._secondary_position
	
	@secondary_position.setter
	def secondary_position(self, new_secondary_position):
		self._secondary_position = new_secondary_position
		
		if new_secondary_position is not None:
			self.statistics.num_moves_to_new_secondary_position += 1
			self.statistics.secondary_positions_visit_counter[next(i for i, p in enumerate(comperf + honorific) if p["PosID"] == new_secondary_position)] += 1
		
		assert(new_secondary_position == None or len(list(p for p in comperf + honorific if p["PosID"] == new_secondary_position)) >= 1)
	
	def has_secondary_position(self):
		return self.secondary_position != None
	
	def get_secondary_position_props(self):
		assert(self.has_secondary_position())
		return next((p for p in comperf + honorific if p["PosID"] == self.secondary_position))
	
	def is_ranked(self):
		return self.get_position_props()["rankint"] != 0
	
	def has_commission(self):
		return self.has_secondary_position() and self.get_secondary_position_props()["Type"] == "Commission"
	
	def has_finished(self):
		return self.get_position_props()["Type"] == "Final"
	
	def is_in_performance_review(self):
		return self.has_secondary_position() and self.get_secondary_position_props()["Type"] == "Performance"
	
	def is_eligible_for_xieban(self):
		return self.is_manchu or self.is_hanlin
	
	def is_eligible_for_yushi(self):
		return self.is_manchu or self.is_juren
	
	def is_eligible_for_zongcai(self):
		return (not self.is_juanban) or self.is_jinshi
	
	def get_final_statistics(self):
		self.statistics.money_to_pool = self.money_to_pool
		self.statistics.money_from_pool = self.money_from_pool
		self.statistics.money_to_players = self.money_to_players
		self.statistics.money_from_players = self.money_from_players
		if self.is_ranked():
			self.statistics.final_rankint = self.rankint
		
		return self.statistics
	
	""" Return a list of all targets that could be bought from the player's 
		current position, together with the price that would have to be
		paid. This is our own rule. """
	def get_potential_purchase_targets(self):
		""" Chushen from which a C1-出身: P11-監生 has to be bought first. """
		purchase_jiansheng_positions = ["C0-局外：P0-白丁",
			"C1-出身：P8-天文生",
			"C1-出身：P9-醫士",
			"C1-出身：P10-生員",
			"C1-出身：P13-供事",
			"C1-出身：P14-吏員",
			"C1-出身：P15-童生"]
		
		""" Check whether the player has to purchase 監生 first. 
			In our rules, this is the case if they do not have a rank
			yet and come from certain chushen. """
		if not (self.is_ranked() or self.position == "C1-出身：P11-監生") and (self.is_outside_board() or \
			self.statistics.first_position in purchase_jiansheng_positions):
				""" Astronomers and physicians can't purchase after
					they have moved from their chushen. """
				if "C39-太醫院" in self.position or \
					"C40-欽天監" in self.position:
						return []
				else:
					return [("C1-出身：P11-監生",
						2 if self.statistics.first_position == "C1-出身：P10-生員" else 5)]
		else:
			""" Otherwise, all positions in 捐班 can be purchased that are 
				ranked higher than the current rank of the player. The fee
				is 5 times the difference in rank"""
			effective_rankint = self.rankint if self.is_ranked() else 0
			return [(p["PosID"], 5 * (p["rankint"] - effective_rankint)) for p in positions
				if "捐班" in p["Department"] and (not self.is_ranked() or p["rankint"] > effective_rankint)]

		
""" Class that models the state of the whole game. """
class Game:
	def __init__(self, num_players, purchase_strategy):
		""" State of the players in the game """
		self.players = [Player(purchase_strategy) for _ in range(num_players)]
		
		""" In the beginning, every player has to pay 100 into the pool. """
		self.pool_money = 100 * num_players
		for p in self.players:
			p.money_to_pool = 100
	
	def all_players_finished(self):
		return all(p.has_finished() for p in self.players)
	
	def is_finished(self):
		""" By our own decision, we consider a game over if there either 
			no player remaining, or if there is exactly one player remaining,
			but the pool has run out of money. """
		return self.all_players_finished() or \
			(self.pool_money < 5 and sum(1 for p in self.players if p.has_finished()))
	
	""" Move all players that are not already finished to final positions
		appropriate to their current rank. If they are in 革留 or 交部 
		positions, they first have to pay a fine. (See Puk p. 30) """
	def move_remaining_players_to_retirement(self): 
		for p in self.players:
			if not p.has_finished():
				if p.secondary_position in ["C13-處分：P78-交部", "C13-處分：P79-革留"]:
					print_game_state(f"Player #{self.players.index(p)} is in position {p.secondary_position}, pay a fine before going to retirement.")
					self.player_to_pool(p, p.rankint * 3)
				p.secondary_position = None
				if not p.is_ranked() or p.rankint <= 1:
					print_game_state(f"Player #{self.players.index(p)} rank is not sufficient for a position in the 品級考. Move outside gameboard instead.")
					p.position = "C0-局外：P0-白丁"
				else:
					p.position = get_retirement_position(p.rankint)
					print_game_state(f"Player #{self.players.index(p)} retired into {p.position}")
	
	""" Handle payment of amount money from all players still in the game
		to target_player """
	def add_player_money(self, target_player, amount):
		""" Amount that is effectively paid to the receiving player by the
			other players. """
		effective_amount = 0
		
		for p in self.players:
			if p is not target_player:
				if not p.has_finished():
					effective_amount += amount
					p.money_to_players += amount
		
		target_player.money_from_players += effective_amount
	
	def pool_to_player(self, player, amount):
		if self.pool_money < amount:
			""" If the pool runs out of money, all players have to
				contribute to fill it again. This is an interpolation
				by Puk (p. 25). The amount they contribute is decided
				by us. """
			print_game_state("Not enough money in the pool. All players not finished need to contribute to fill the pool again.")
			for p in self.players:
				if not p.has_finished():
					self.pool_money += 25
					p.money_to_pool += 25
			self.pool_to_player(player, amount)
		else:
			self.pool_money -= amount
			player.money_from_pool += amount
			
	def player_to_pool(self, player, amount):
		self.pool_money += amount
		player.money_to_pool += amount
	
	""" Handle the 見禮 system: if a player has arrived at a board where 
		there already is another player at a higher position, they have
		to pay 5 money to the other player. """
	def handle_jian_li(self, p):
		""" p is the player who has just moved, and whose position is 
			already at the new position. """
		
		""" TODO: Are there other departments that should be excluded here? """
		if p.get_position_props()["Department"] in ["品級考"]:
			return
		for q in self.players:
			if p is not q:
				if p.get_position_props()["Department"] == q.get_position_props()["Department"]:
					if (p.is_ranked() and not q.is_ranked()) or \
						(p.is_ranked() and q.is_ranked() and p.rankint > q.rankint):
						print_game_state(f"Player #{self.players.index(p)} has encountered junior player #{self.players.index(q)} at {p.get_position_props()['Department']}, receive 5 money.")
						p.money_from_players += 5
						q.money_to_players += 5
					elif (p.is_ranked() and not q.is_ranked()) or \
						(p.is_ranked() and q.is_ranked() and p.rankint > q.rankint):
						print_game_state(f"Player #{self.players.index(p)} has encountered senior player #{self.players.index(q)} at {p.get_position_props()['Department']}, pay 5 money.")
						p.money_to_players += 5
						q.money_from_players += 5

	""" Distribute final money. """
	def distribute_final_money(self):
		print_game_state("Game finished, commencing final money distribution.")
		
		""" We start by equally distributing the remaining money in the pool. """
		print_game_state(f"Every player receives {self.pool_money / len(self.players)} money from the pool.")
		for p in self.players:
			p.money_from_pool += self.pool_money / len(self.players)
		self.pool_money = 0
		
		""" Iterate over all pairs of players to compute how much each 
			of them has to pay to the others. """
		for i in range(len(self.players)):
			for j in range(len(self.players)):
				p = self.players[i]
				q = self.players[j]
				if p is not q:
					""" If both don't have a rank then skip this pair."""
					if not p.is_ranked() and not q.is_ranked():
						continue
					
					p_rank = None
					q_rank = None
					if p.is_ranked():
						p_rank = p.rankint
					else:
						""" If a player doesn't have a rank, then they are  
							treated as if they had rankint 1. See Puk p. 30""" 
						p_rank = 1
					if q.is_ranked():
						q_rank = q.rankint
					else:
						q_rank = 1
					
					if p_rank == q_rank:
						print_game_state(f"Players #{i} and #{j} have the same rank, so neither of them needs to pay to the other.")
					elif p_rank > q_rank:
						money = 5 * (p_rank - q_rank)
						print_game_state(f"Player #{i} receives {money} from player #{j}")
						p.money_from_players += money
						q.money_to_players += money
					else:
						money = 5 * (q_rank - p_rank)
						print_game_state(f"Player #{j} receives {money} from player #{i}")
						q.money_from_players += money
						p.money_to_players += money
		
		""" Sanity check: the total amount of money paid by players should 
			be the same as the amount received by them. """
		total_paid = 0
		total_received = 0
		total_pool = 0
		for p in self.players:
			total_paid += p.money_to_players
			total_received += p.money_from_players
			total_pool += p.money_from_pool - p.money_to_pool
		assert(total_paid == total_received)
		assert(total_pool == 0)

""" Order in which dice faces have to be processed in, i.e. 德 is the first 
	that is checked for and so on. This is according to rule 1.5. """ 
dice_processing_order = (4, 6, 5, 3, 2, 1)

""" Name of a move that is associated with a particular face of a dice. """
moves_by_dice = ("賍", "柔", "良", "德", "功", "才")

""" Chinese character for dice face. """
dice_to_chinese = ("幺", "二", "三", "四", "五", "六")

""" English names of the moves """
move_to_english = { "賍": "corrupt", "柔": "weak", "良": "good", "德": "virtuous", "功": "meritorious", "才": "talented" }

""" Return the moves that are associated with a certain dice combination.
	The result is a (possibly empty) list of up to two moves in the order
	in which they shall be executed in.""" 
def dice_to_moves(dices):
	moves = []
	
	""" Check if there are two distinct pairs of the same color
	(1, 4 = red) (all other = black) """
	for a in range(1, 7):
		for b in range(a + 1, 7):
			if dices.count(a) == 2 and dices.count(b) == 2:
				if a == 1 and b == 4:
					return ["紅二對"]
				elif a != 1 and a != 4 and b != 4:
					return [f"素二對{a}{b}"]
	
	""" Loop through all possible face values in the sequence defined in
		rule 1.5. """
	for a in dice_processing_order:
		if dices.count(a) == 2:
			""" According to rule 1.3, a 4 cancels two 1s """
			if a == 1 and 4 in dices:
				pass
			else:
				""" Indices to moves_by_dice start at 0, so subtract 
					one from the face value. """
				moves.append(moves_by_dice[a - 1])
		elif dices.count(a) == 3:
			""" According to rule 1.4, a 4 even cancels three 1s. 
				This might be interpolation by Puk Wing Kin, as
				the rule on the board only states "兩幺帶有一四免行賍" """
			if a == 1 and 4 in dices:
				pass
			else:
				""" By rule 1.4, three dice with the same face make two 
					moves """
				moves.append(moves_by_dice[a - 1])
				moves.append(moves_by_dice[a - 1])
		elif dices.count(a) == 4:
			moves.append(f"全色{a}")
	
	if 3 in dices and 4 in dices and 5 in dices and 6 in dices:
		moves.append("穿花")
	
	return moves

""" Return the moves that are associated with a certain dice combination
	for someone who is outside the game board. This is either None or
	a string that defines the move. """
def dice_to_move_chu_shen(dices):
	""" Check if there are two distinct pairs of the same color
	(1, 4 = red) (all other = black) """
	for a in range(1, 7):
		for b in range(a + 1, 7):
			if dices.count(a) == 2 and dices.count(b) == 2:
				if a == 1 and b == 4:
					return "紅二對"
				elif a != 1 and a != 4 and b != 4:
					return f"素二對"
	
	""" Check for single pairs / triples / quadruplets. Since we handled 
		double pairs above, processing order does not matter here. """
	for a in range(1, 7):
		if dices.count(a) == 2:
			return "雙" + dice_to_chinese[a - 1]
		elif dices.count(a) == 3:
			return "聚" + dice_to_chinese[a - 1]
		elif dices.count(a) == 4:
			return f"全色{a}"
	
	if 3 in dices and 4 in dices and 5 in dices and 6 in dices:
		return "穿花"
	
	return None

""" Returns whether the given move is considered "lucky", that is,
	either a quadruplet or 穿花 """
def is_lucky_move(move):
	return move == "穿花" or move.startswith("全色") or move == "紅二對" or move.startswith("素二對")

""" Decomposes a lucky move into the default actions taken for it. """
def decompose_lucky_move(move):
	assert(is_lucky_move(move))
	if move == "穿花":
		""" According to rule 2.4 """
		return ["才"]
	elif move == "全色1":
		""" According to rule 5.4 """
		return ["德", "才"]
	elif move == "全色2":
		return ["德"] * 2
	elif move == "全色3":
		return ["德", "德", "功"]
	elif move == "全色4":
		return ["德"] * 4
	elif move == "全色5":
		return ["德", "德", "才"]
	elif move == "全色6":
		return ["德"] * 3
	elif move == "紅二對":
		""" 紅二對 is two fours and two ones. Hence, the 贓 gets cancelled. """
		return ["德"] 
	elif move.startswith("素二對"):
		""" For 素二對, the actual dice are appended to the move in ascending
		    order. """
		assert(len(move) == 5)
		return [moves_by_dice[int(move[-1]) - 1], moves_by_dice[int(move[-2]) - 1]]

""" Try to find a specific lucky relation starting from a particular position. """
def find_lucky_relation(position, move):
	assert(is_lucky_move(move))
	""" For 素二對, we store the actual dice in the end of the string, so
		remove them here in order to perform the look-up in the table. """
	effective_move = move[:3] if move.startswith("素二對") else move
	rst = list(r for r in luckyrels0 + luckyrels1 + luckyrels2 + luckyrels3 if r["SourceID"] == position and r["Dice"] == effective_move)
	if len(rst) == 0:
		return None
	else:
		assert(len(rst) == 1)
		return rst[0]

""" Try to find a relation from a secondary position by a certain move. """
def find_secondary_relation(position, move):
	rst = list(r for r in comperfrels2 + comperfrels3 if r["SourceID"] == position and r["Dice"] == move)
	if len(rst) == 0:
		return None
	else:
		assert(len(rst) == 1)
		return rst[0]

""" Get the appropriate retirement position id for a given rankint. """
def get_retirement_position(rankint):
	rst = list(p for p in positions if p["Type"] == "Final" and p["rankint"] == rankint)
	assert(len(rst) == 1)
	return rst[0]["PosID"]

""" Get an automatic move relation from a position, e.g. for 'C2-世爵：P16-衍聖公'. """
def find_auto_relation(position):
	rst = list(r for r in uniquerels if r["SourceID"] == position and r["Dice"] == "Auto")
	if len(rst) == 0:
		return None
	else:
		assert(len(rst) == 1)
		return rst[0]

""" Function that executes one turn for a single player. """
def process_player_turn(game, player):
	purchase = player.purchase_strategy(game, player)
	
	if purchase is not None:
		print_game_state(f"Purchase office {purchase[0]} for {purchase[1]} money.")
		player.position = purchase[0]
		game.player_to_pool(player, purchase[1])
		player.statistics.has_purchased_office = 1
		game.handle_jian_li(player)
	else:
		dices = list(random.randint(1, 6) for _ in range(4))
		player.statistics.num_dice_rolls += 1
		print_game_state(f"Rolled dices {', '.join((str(d) for d in dices))}")
		
		if player.is_outside_board():
			print_game_state("Player is outside gameboard.")
			move = dice_to_move_chu_shen(dices)
			if move != None:
				print_game_state(f"Move: {move}")  
				process_move_into_gameboard(game, player, move)
			else:
				print_game_state(f"This combination of dice does not constitute a move. Wait a turn.")
		else:
			moves = dice_to_moves(dices)
			if len(moves) > 0:
				print_game_state(f"The dice roll means the player has to take the move(s): {', '.join(moves)}")
			else:
				print_game_state(f"This combination of dice does not constitute a move. Wait a turn.")
			process_player_moves(game, player, moves)
	print_game_state("End of turn.\n")


""" Function that executes a single move that takes the player from
	outside the gameboard to one of the starting positions. """
def process_move_into_gameboard(game, player, move):
	assert(player.is_outside_board())
	rels = list(r for r in luckyrels0 if r["SourceID"] == player.position and r["Dice"] == move)
	if len(rels) != 1:
		print_game_state(f"Failed to find initial position for move '{move}'")
		sys.exit(-1)
	
	rel = rels[0]
	if rel["pool"] != 0:
		print_game_state(f"Draw {rel['pool']} money from the pool.")
		game.pool_to_player(player, rel["pool"])
	
	if rel["player"] != 0:
		print_game_state(f"Collect {rel['player']} money from the other players.")
		game.add_player_money(player, rel["player"])
	
	print_game_state(f"Move token to {rel['TargetID']}")
	player.position = rel['TargetID']
	process_auto_relation(game, player)

""" Function that executes moves of a player, taking moves from the 
	queue until it runs empty. """
def process_player_moves(game, player, initial_moves):
	moves = initial_moves
	while len(moves) > 0 and not player.has_finished():
		move = moves.pop(0)
		""" Processing a move returns a (potentially empty) list of new
			moves that have to be prepended to the queue of moves to be taken """
		new_moves = process_player_move(game, player, move)
		if len(new_moves) > 0:
			print_game_state(f"Prepending {', '.join(new_moves)} to move queue, move queue is now {', '.join(new_moves + moves)}")
			moves = new_moves + moves

""" Function that executes a single move of a player, returning a potentially
	empty list of moves that shall be executed next """
def process_player_move(game, player, move):
	if player.has_secondary_position():
		print_game_state(f"Performing move '{move}' from position '{player.secondary_position}'")
		
		""" For secondary positions, there is either an action, e.g. 
			taking another move, or paying a fine and returning to the
			original position, or there is a relation that defines a move
			to another secondary position. """ 
		action = None
		relation = None
		
		if is_lucky_move(move):
			if move == "穿花":
				if "garland" in player.get_secondary_position_props():
					action = player.get_secondary_position_props()["garland"]
					if action == "":
						action = None
				
			relation = find_lucky_relation(player.secondary_position, move)
			
			""" If there is no particular rule for this lucky move,
				handle it according to the default rules. """
			if action == None and relation == None:
				print_game_state(f"No specific rule found for lucky move '{move}' in this position, proceeding according to default rule.")
				return decompose_lucky_move(move)
			else:
				player.statistics.num_moves += 1
				player.statistics.num_moves_by_type[-1] += 1
				
				""" If the action is 下一, i.e. go down one position,
					it is in fact a relation that should be in the
					table. """
				if action == "下一":
					action = None
					assert(relation != None)
				
				assert(action == None or relation == None)
				
				if action != None:
					return process_secondary_action(game, player, action, move)
				else:
					process_secondary_relation(game, player, relation)
					return []
		else:
			player.statistics.num_moves += 1
			player.statistics.num_moves_by_type[moves_by_dice.index(move)] += 1
			
			action = None
			relation = None
			action = player.get_secondary_position_props().get(move_to_english[move])
			if action == "":
				action = None
			relation = find_secondary_relation(player.secondary_position, move)
			
			""" If the action is 下一, i.e. go down one position,
					it is in fact a relation that should be in the
					table. """
			if action == "下一":
				action = None
				assert(relation != None)
			
			""" There should be either an action or a relation, but not both.
				However, if the action is '不行', there might be a relation
				that just goes back to the same position, which we ignore
				here. """
			assert((not (action != None and relation != None)) or (action == "不行" and relation["TargetID"] == player.secondary_position))
			
			if action == None and relation == None:
				print_game_state("There is no prescription what to do with this move at this position. Skip a turn.")
				return []
			elif action != None:
				return process_secondary_action(game, player, action, move)
			else:
				process_secondary_relation(game, player, relation)
				return []
	else: # No secondary position
		""" For a player in the positions "C39-太醫院：P241-院使" and "C40-欽天監：P247-監正"
			some moves only result in an increment in rank while
			staying at the same position. """
		if player.position in ("C39-太醫院：P241-院使", "C40-欽天監：P247-監正") and move in ("德", "才", "穿花"):
			player.statistics.num_moves += 1
			player.statistics.num_moves_by_type[moves_by_dice.index(move) if move != "穿花" else -1] += 1
			
			process_special_rank_move(game, player, move)
			return []
		elif is_lucky_move(move):
			relation = find_lucky_relation(player.position, move)
			if relation != None:
				player.statistics.num_moves += 1
				player.statistics.num_moves_by_type[-1] += 1
				
				process_relation(game, player, relation)
				return []
			else:
				print_game_state(f"No specific rule found for lucky move '{move}' in this position, proceeding according to default rule.")
				return decompose_lucky_move(move)
		else:
			player.statistics.num_moves += 1
			player.statistics.num_moves_by_type[moves_by_dice.index(move)] += 1
			
			relations = list(r for r in uniquerels + comperfrels1 if r["SourceID"] == player.position and r["Dice"] == move)
			special_relation_target = set(("C57-內閣：P353-協辦大學士", "C50-都察院：P309-監察御史", "C50-都察院：P310-巡街御史",
				"C5-會試：P41-總裁", "C4-鄉試：P34-主考", "C4-鄉試：P35-同考", "C5-會試：P42-同考")).intersection(set(r["TargetID"] for r in relations))
			assert(len(special_relation_target) <= 1)
			if (player.position in xieban_origin_positions or player.position in yushi_origin_positions or\
				player.position in zongcai_origin_positions) and len(special_relation_target) == 1:
				""" There are two possible relations, depending on whether
					the player has the right to become the respective position. """
				assert(len(relations) == 2)
				special_relation_target = special_relation_target.pop()
				if player.position in xieban_origin_positions and special_relation_target == "C57-內閣：P353-協辦大學士":
					if player.is_eligible_for_xieban():
						process_relation(game, player, next(r for r in relations if r["TargetID"] == special_relation_target))
					else:
						print_game_state("Background is insufficient to become 協辦, go to retirement instead.")
						process_relation(game, player, next(r for r in relations if r["TargetID"] != special_relation_target))
				elif player.position in yushi_origin_positions and\
					special_relation_target in ("C50-都察院：P309-監察御史", "C50-都察院：P310-巡街御史"):
					if player.is_eligible_for_yushi():
						process_relation(game, player, next(r for r in relations if r["TargetID"] == special_relation_target))
					else:
						print_game_state(f"Background is insufficient to become '{special_relation_target}'.")
						process_relation(game, player, next(r for r in relations if r["TargetID"] != special_relation_target))
				else:
					if player.is_eligible_for_zongcai():
						process_relation(game, player, next(r for r in relations if r["TargetID"] == special_relation_target))
					else:
						print_game_state(f"Background is insufficient to become '{special_relation_target}'.")
						process_relation(game, player, next(r for r in relations if r["TargetID"] != special_relation_target))
				return  []
			elif (player.position, move) in refusable_moves:
				print_game_state("In the real game, taking this move from this position could be refused.")
				print_game_state("However, we always take it.")
				relation = list(r for r in uniquerels + comperfrels1 if r["SourceID"] == player.position and r["Dice"] == move and r["TargetID"] != player.position)
				assert(len(relation) == 1)
				process_relation(game, player, relation[0])
				return []
			elif player.position in ("C39-太醫院：P241-院使", "C40-欽天監：P247-監正") and move in ("德", "才"):
				process_special_rank_move(game, player, move)
				return []
			else:
				relation = find_relation(player.position, move)
				if relation == None:
					print_game_state("There is no prescription what to do with this move at this position. Skip a turn.")
				else:
					process_relation(game, player, relation)
				return []

def rankint_to_ranktrad(rankint):
	assert(rankint > 0)
	if rankint == 1:
		return "10"
	else:
		baserank = 10 - rankint // 2
		assert(baserank > 0)
		if rankint % 2 == 0:
			return str(baserank) + "b"
		else:
			return str(baserank) + "a"

""" For a few moves in "太醫院" and "欽天監", the player does not
	change position but still gets a new rank. We handle this here. """
def process_special_rank_move(game, player, move):
	if move == "德" and player.rankint < 16:
		print_game_state(f"Executing '{move}' from '{player.position}': only increase the rank by two, but do not move.")
		player.increase_special_rankint(2)
	else:
		print_game_state(f"Executing '{move}' from '{player.position}': only increase the rank by one, but do not move.")
		player.increase_special_rankint(1)
	
	print_game_state(f"New rank: {rankint_to_ranktrad(player.rankint)}")
	
	""" If the player reaches a rank of 2a, they go to retirement."""
	if player.rankint >= 17:
		print_game_state("After having reached this rank, go to retirement (大賀).")
		print_game_state("Draw 30 money from each player still in the game.")
		game.add_player_money(player, 30)
		player.secondary_position = None
		player.position = get_retirement_position(player.rankint)
		print_game_state(f"Retired in position '{player.position}'.")


""" For some secondary positions, the game prescribes an action that can
	consist of e.g. additional moves to be executed, or paying a fine and
	so on. This function handles such actions. The parameter 'original_move'
	is the move that has caused this action to be executed (needed for
	原行). The return value is a list of further moves that have to be
	executed. """
def process_secondary_action(game, player, action, original_move):
	if action == "不行" or action == "停選":
		print_game_state(f"Action is '{action}', don't do anything.")
		return []
	elif all((i in moves_by_dice for i in action.split("/"))):
		moves = action.split("/")
		print_game_state(f"Remove token from secondary position and perform {', '.join(moves)} from original position.")
		player.secondary_position = None
		return moves
	elif action == "原行":
		print_game_state(f"Action is '原行', remove token from secondary position and perform '{original_move}' from original position.")
		player.secondary_position = None
		return [original_move]
	elif action in ("免", "回任") or (player.has_commission() and action in ("回", "銷去")):
		assert(player.has_commission())
		print_game_state(f"Action is '{action}', repay the 5 money received for the commission and remove token from secondary position.")
		game.player_to_pool(player, 5)
		player.secondary_position = None
		return []
	elif action == "罰回":
		print_game_state("Action is '罰回', pay a fine of 10 and remove token from secondary position.")
		game.player_to_pool(player, 10)
		player.secondary_position = None
		return []
	elif action == "倍罰回":
		print_game_state("Action is '罰回', pay a fine of 15 and remove token from secondary position.")
		game.player_to_pool(player, 15)
		player.secondary_position = None
		return []
	elif action in ("回", "銷去") and player.is_in_performance_review():
		""" 回 and 銷去 can occur both for commissions and performance positions. 
		It needs to be handled differently, because for commissions,
		the money the player obtained for the commission needs to be
		deducted again. """
		print_game_state("Action is '銷去', remove token from secondary position.")
		player.secondary_position = None
		return []
	elif action == "復任" or action == "恩復":
		print_game_state(f"Action is '{action}', remove token from secondary position.")
		player.secondary_position = None
		return []
	elif action == "贖罪復任":
		fine = 3 * player.rankint
		print_game_state(f"Action is '贖罪復任', pay a fine of {fine} and remove token from secondary position.")
		game.player_to_pool(player, fine)
		player.secondary_position = None
		return []
	elif action == "罰俸復任":
		fine = player.rankint
		print_game_state(f"Action is '罰俸復任', pay a fine of {fine} and remove token from secondary position.")
		game.player_to_pool(player, fine)
		player.secondary_position = None
		return []
	elif action in ["賀", "大賀", "原品休致", "加一級榮歸"]:
		"""Retirements"""
		
		player_money = 0
		
		if action == "大賀":
			player_money = 30
		elif action == "加一級榮歸":
			player_money = 10
		
		print_game_state(f"Action is '{action}', {'receive ' + str(player_money) + ' money from each player still in the game and ' if player_money > 0 else ''}go to retirement.")

		game.add_player_money(player, player_money)
		player.secondary_position = None
		
		rankint = player.rankint
		
		if action == "加一級榮歸":
			print_game_state("Retire one rank higher than original rank.")
			rankint += 1
		
		""" For 原品休致 it can happen that the player did not hold a rank.
			Handle this case specially. """
		if rankint == 1:
			print_game_state("Did not have a rank yet, so move out of board.")
			player.position = "C0-局外：P0-白丁"
		else:
			player.position = get_retirement_position(rankint)
			print_game_state(f"Retired in position '{player.position}'.")
		return []
	else:
		print_game_state(f"Error: Don't know how to handle action '{action}' from position '{player.secondary_position}'")
		raise Exception("Don't know how to proceed, aborting.")

""" Process monetary aspects of a relation. """
def process_relation_money(game, player, relation, has_changed_primary_position):
	if relation["pool"] > 0:
		game.pool_to_player(player, relation["pool"])
		print_game_state(f"Draw {relation['pool']} money from the pool")
	if relation["player"] > 0:
		game.add_player_money(player, relation["player"])
		print_game_state(f"Draw {relation['player']} from the other players.")
	
	if has_changed_primary_position:
		game.handle_jian_li(player)

""" Process a relation that goes from a secondary position to somewhere else. """
def process_secondary_relation(game, player, relation):
	target = relation["TargetID"]
	""" A relation from a secondary position might lead to both a regular
		and a secondary position. In the first case, the secondary token
		is removed from the board. """
	if len(list(p for p in positions if p["PosID"] == target)) > 0:
		print_game_state(f"Remove secondary token, move primary token to new position: '{target}'.")
		player.secondary_position = None
		player.position = target
		process_auto_relation(game, player)
		process_relation_money(game, player, relation, True)
	else:
		print_game_state(f"Move secondary token to new position: '{target}'.")
		player.secondary_position = target
		process_relation_money(game, player, relation, False)

""" Process a relation that goes from a regular position to somewhere else. """
def process_relation(game, player, relation):
	target = relation["TargetID"]
	
	if is_secondary_position(target):
		print_game_state(f"Move secondary token to new position: '{target}'.")
		player.secondary_position = target
		process_relation_money(game, player, relation, False)
	else:
		print_game_state(f"Move token to new position: '{target}'.")
		player.position = target
		process_relation_money(game, player, relation, True)
		process_auto_relation(game, player)

""" For some positions such as 'C2-世爵：P16-衍聖公', the player automatically
    moves to another position. This is handled in this procedure. """
def process_auto_relation(game, player):
	relation = find_auto_relation(player.position)
	if relation != None:
		print_game_state(f"From position '{player.position}', move automatically to new position '{relation['TargetID']}'.")
		player.position = relation['TargetID']
		process_relation_money(game, player, relation, True)

""" Check whether a given position ID belongs to a regular or secondary position. """
def is_secondary_position(pos_id):
	return len(list(p for p in positions if p["PosID"] == pos_id)) == 0

""" Try to find a relation from a position with a certain move. """
def find_relation(position, move):
	rst = list(r for r in uniquerels + comperfrels1 if r["SourceID"] == position and r["Dice"] == move)
	if len(rst) == 0:
		return None
	else:
		assert(len(rst) == 1)
		return rst[0]

# Code to check sanity of the CSV files
if __name__ == "__main__":
	""" Check whether for all positions, there is a relation for every move
		in the database. """
	for position in positions:
		position_id = position["PosID"]
		
		if position_id == "C0-局外：P0-白丁" or position["Type"] == "Final":
			pass
		elif len(list(r for r in uniquerels if r["SourceID"] == position_id and r["Dice"] == "Auto")) == 1:
			""" Some positions such as 'C2-世爵：P16-衍聖公' move automatically 
			    to another position """
			pass
		else:
			for move in moves_by_dice:
				relations = list(r for r in uniquerels + comperfrels1 if r["SourceID"] == position_id and r["Dice"] == move)
				
				if (position_id in xieban_origin_positions and move == "德") or \
					(position_id in yushi_origin_positions and\
						len(set(("C50-都察院：P309-監察御史", "C50-都察院：P310-巡街御史")).intersection(set(r["TargetID"] for r in relations))) != 0) or \
					(position_id in zongcai_origin_positions and\
						len(set(("C5-會試：P41-總裁", "C4-鄉試：P34-主考", "C4-鄉試：P35-同考", "C5-會試：P42-同考")).intersection(set(r["TargetID"] for r in relations))) != 0):
					""" There is a special rule for these relations, in 
						that they are only permitted for certain people.
						Hence, there exists an alternative relation
						in the database. """
					assert(len(relations) == 2)
				elif (position_id, move) in refusable_moves:
					""" Refusable moves """
					assert(len(relations) <= 2)
				else:
					if len(relations) == 0:
						print_game_state(f"Warning: No successor for position '{position_id}' and move '{move}' found in database.")
					elif len(relations) > 1:
						print_game_state(f"Warning: Position '{position_id}' has multiple successors for move '{move}' in database.")
						print_game_state("Relationships are:")
						print_game_state(relations)
						print_game_state("")

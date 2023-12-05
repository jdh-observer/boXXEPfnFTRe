
class PlayerStatistics:
	def __init__(self):
		""" First position the player held. """
		self.first_position = None
		
		""" Number of dice rolls. """
		self.num_dice_rolls = 0
		
		""" Number of moves executed, including those that had no consequences. """
		self.num_moves = 0
		
		""" Number of moves of the respective type taken, in the order of
			moves_by_dice, plus lucky """
		self.num_moves_by_type = [0, 0, 0, 0, 0, 0, 0]
		
		""" Number of moves to new primary positions. """
		self.num_moves_to_new_position = 0
		
		""" Number of moves to new secondary positions. """
		self.num_moves_to_new_secondary_position = 0
		
		""" Amount of money taken draw from / paid to pool. """
		self.money_to_pool = 0
		self.money_from_pool = 0
		
		""" Amount of money that had to be paid to this player by other players and vice versa. """
		self.money_to_players = 0
		self.money_from_players = 0
		
		""" Final rankint. """
		self.final_rankint = None
		
		""" Whether player has ever purchased office. """
		self.has_purchased_office = 0
		
		""" Whether strategy would have suggested player purchase office,
			but he did not. """
		self.should_have_purchased_office = 0
		
		""" Whether the player has visited a position with the type
			'exam'. """
		self.has_visited_exam = 0
		
		""" When using 'late' or 'catchup' strategy, was the player
			in a position marked 'Exam' when the strategy applied
			(not necessarily leading to a purchase) """
		self.was_in_exam_when_purchase_strategy_applied = 0
		
		self.positions_visit_counter = 338 * [0]
		self.secondary_positions_visit_counter = (38 + 49 + 36) * [0]
		
	def effective_money(self):
		return -self.money_to_pool + self.money_from_pool - self.money_to_players + self.money_from_players
	
	def serialize(self):
		assert(not (self.has_purchased_office and self.should_have_purchased_office))
		return ",".join((str(i) for i in [self.first_position, self.num_dice_rolls, self.num_moves, self.num_moves_to_new_position, self.money_to_pool,
			self.money_from_pool, self.money_to_players, self.money_from_players, self.final_rankint, self.has_purchased_office, self.should_have_purchased_office,
			self.has_visited_exam, self.was_in_exam_when_purchase_strategy_applied]\
			+ self.num_moves_by_type\
			+ self.positions_visit_counter\
			+ self.secondary_positions_visit_counter))
	
	@staticmethod
	def from_line(line):
		parts = line.split(",")
		rst = PlayerStatistics()
		rst.first_position = parts[0]
		(rst.num_dice_rolls, rst.num_moves, rst.num_moves_to_new_position,
			rst.money_to_pool, rst.money_from_pool, rst.money_to_players,
			rst.money_from_players, rst.final_rankint, rst.has_purchased_office,
			rst.should_have_purchased_office, rst.has_visited_exam,
			rst.was_in_exam_when_purchase_strategy_applied) = \
			(float(i) for i in parts[1:13])
		rst.num_moves_by_type = list(int(i) for i in parts[13:20])
		rst.positions_visit_counter = list(int(i) for i in parts[20:20 + 338])
		rst.secondary_position_visit_counter = list(int(i) for i in parts[20 + 338:])
		return rst

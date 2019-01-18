class Solution:
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """

        if not asteroids:
            return asteroids

        # Stack to keep track of the left asteroids
        stack = []

        # Iterate through the asteroids array from left to right
        for ast in asteroids:
            # If the stack top element is greater than zero,
            # and the incoming asteroid is negative there would be collision.
            # Remove the asteroid which explodes in this collision, and keep repeating
            # the step until the incoming negative asteroid survives the collision.
            while stack and stack[-1] > 0 and ast < 0:
                # If incoming asteroid has greater magintude, it will survive, and can
                # further collide with other positive asteroids in the stack.
                if -ast > stack[-1]:
                    # Remove the current top element of the stack as it exploded.
                    stack.pop()
                    continue
                # If both have equal magnitude, we don't push the incoming asteroid
                # to the stack, and also remove the stack top. Since both exploded.
                if -ast == stack[-1]:
                    stack.pop()
                # When the incoming asteroid has smaller magnitude, we let
                # the top of stack remain intact and break out of the loop.
                break
            else: stack.append(ast)

        return stack

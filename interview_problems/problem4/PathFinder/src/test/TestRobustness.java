package test;
import org.junit.*;
import java.util.*;

public class TestRobustness extends AbstractTest
{
	@Test
	public void nullList()
	{
		List<Integer> list = null;
		int pos = 0;
		test(list, pos);
	}

	@Test
	public void emptyList()
	{
		List<Integer> list = Arrays.asList();
		int pos = 0;
		test(list, pos);
	}

	@Test
	public void invalidStartingPosition()
	{
		List<Integer> list = Arrays.asList(1, 2, 0);
		int pos = 7;
		test(list, pos, -1);
	}

	@Test
	public void negativeStartingPosition()
	{
		List<Integer> list = Arrays.asList(1, 2, 0);
		int pos = -1;
		test(list, pos, -1);
	}

	@Test
	public void startInTheMiddle()
	{
		List<Integer> list = Arrays.asList(0, 1, 2, 0, 1);
		int pos = 2;
		test(list, pos);
	}

	@Test
	public void nullValuesInList()
	{
		List<Integer> list = Arrays.asList(1, 3, null, 2, null);
		int pos = 1;
		test(list, pos);
	}

	@Test
	public void negativeJump()
	{
		List<Integer> list = Arrays.asList(0, 2, -2, 2, 1);
		int pos = 2;
		test(list, pos);
	}

	@Test
	public void avoidCycles()
	{
		List<Integer> list = Arrays.asList(4, -1, 4, 1, -1, 2, -2);
		int pos = 1;
		test(list, pos);
	}
}

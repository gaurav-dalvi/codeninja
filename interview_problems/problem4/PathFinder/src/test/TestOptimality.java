package test;
import org.junit.*;
import java.util.*;

public class TestOptimality extends AbstractTest
{
	@Test
	public void shortestPath1()
	{
		List<Integer> list = Arrays.asList(4, 1, 1, 4, 1, 1, 3, 1, 1, 2, 1);
		int pos = 0;
		test(list, pos, 4);
	}

	@Test
	public void shortestPath2()
	{
		List<Integer> list = Arrays.asList(1, 7, 2, 2, -4, 1, 1, 4, -2, 1, 1);
		int pos = 2;
		test(list, pos, 4);
	}

	@Test
	public void shortestPath3()
	{
		List<Integer> list = Arrays.asList(2, 0, 2, 2, 0, 2, 2, 0, 1);
		int pos = 0;
		test(list, pos, 6);
	}
}

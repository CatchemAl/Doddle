from argparse import ArgumentParser, Namespace

from .controller_factory import create_hide_controller, create_solve_controller
from .factory import create_benchmarker, create_simulator
from .solver import SolverType
from .words import Word


def solve(args: Namespace) -> None:

    size = len(args.guess) if args.guess else args.size
    controller = create_solve_controller(size)
    controller.solve(args.guess)


def hide(args: Namespace) -> None:

    size = len(args.guess) if args.guess else args.size
    controller = create_hide_controller(size)
    controller.hide(args.guess)


def run(args: Namespace) -> None:

    solution: Word = args.answer
    guess: Word = args.guess
    depth: int = args.depth
    size = len(solution)

    simulator = create_simulator(
        size,
        solver_type=SolverType.MINIMAX,
        depth=depth,
        extras=[solution, guess],
    )

    simulator.run(solution, guess)


def benchmark_performance(args: Namespace) -> None:

    size: int = len(args.guess) if args.guess else args.size
    depth: int = args.depth
    initial_guess: Word | None = args.guess

    benchmarker = create_benchmarker(
        size,
        solver_type=SolverType.MINIMAX,
        depth=depth,
        extras=[initial_guess],
    )

    benchmarker.run_benchmark(initial_guess)


def main() -> None:

    parser = ArgumentParser()
    subparsers = parser.add_subparsers()

    run_parser = subparsers.add_parser("run")
    run_parser.add_argument("--answer", required=True, type=Word)
    run_parser.add_argument("--guess", type=Word)
    run_parser.add_argument("--depth", required=False, default=1, type=int)
    run_parser.set_defaults(func=run)

    solve_parser = subparsers.add_parser("solve")
    solve_group = solve_parser.add_mutually_exclusive_group()
    solve_group.add_argument("--guess", type=Word)
    solve_group.add_argument("--size", required=False, type=int, default=5)
    solve_parser.add_argument("--depth", required=False, default=1, type=int)
    solve_parser.set_defaults(func=solve)

    hide_parser = subparsers.add_parser("hide")
    hide_group = hide_parser.add_mutually_exclusive_group()
    hide_group.add_argument("--guess", type=Word)
    hide_group.add_argument("--size", type=int, default=5)
    hide_parser.set_defaults(func=hide)

    benchmark_parser = subparsers.add_parser("benchmark")
    benchmark_group = benchmark_parser.add_mutually_exclusive_group()
    benchmark_group.add_argument("--guess", type=lambda s: s.upper())
    benchmark_group.add_argument("--size", type=int, default=5)
    benchmark_parser.add_argument("--depth", required=False, default=1, type=int)
    benchmark_parser.set_defaults(func=benchmark_performance)

    args = parser.parse_args()
    args.func(args)
